import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from urllib.parse import urljoin
import json

class AutocoreScraperProdutos:
    def __init__(self):
        self.base_url = "https://www.autocorerobotica.com.br"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8'
        }
        self.produtos_individuais = []
        
    def get_driver(self):
        """Configura driver Selenium otimizado"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument(f'--user-agent={self.headers["User-Agent"]}')
        
        try:
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception as e:
            print(f"❌ Erro ChromeDriver: {e}")
            return None
    
    def obter_urls_produtos(self):
        """Obtém URLs de páginas de produtos específicos"""
        urls_categorias = [
            f"{self.base_url}/kits",
            f"{self.base_url}/modulos-sensores",
            f"{self.base_url}/componentes-eletronicos",
            f"{self.base_url}/robotica",
            f"{self.base_url}/embarcados",
            f"{self.base_url}/impressao-3d",
            f"{self.base_url}/ferramentas",
            f"{self.base_url}/ofertas"
        ]
        
        urls_produtos = []
        
        for url_categoria in urls_categorias:
            print(f"🔍 Buscando produtos em: {url_categoria}")
            
            try:
                response = requests.get(url_categoria, headers=self.headers, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Buscar links para produtos individuais
                    links_produto = soup.find_all('a', href=re.compile(r'/produto/|/p/|/item/'))
                    
                    for link in links_produto:
                        href = link.get('href')
                        if href:
                            url_completa = urljoin(self.base_url, href)
                            if url_completa not in urls_produtos:
                                urls_produtos.append(url_completa)
                    
                    print(f"   ✅ Encontrados {len(links_produto)} links de produtos")
                else:
                    print(f"   ❌ Erro {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ Erro: {e}")
            
            time.sleep(1)  # Pausa respeitosa
        
        print(f"\n📦 Total de URLs de produtos encontradas: {len(urls_produtos)}")
        return urls_produtos[:50]  # Limitar para teste inicial
    
    def extrair_produto_individual(self, url):
        """Extrai dados de um produto específico"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                return None
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Estratégias para encontrar nome do produto
            nome_produto = None
            seletores_nome = [
                'h1.product-title',
                'h1.produto-titulo', 
                'h1.nome-produto',
                '.product-name h1',
                '.produto-nome h1',
                'h1[class*="title"]',
                'h1[class*="nome"]',
                'title'  # Como fallback
            ]
            
            for seletor in seletores_nome:
                elemento = soup.select_one(seletor)
                if elemento:
                    nome_produto = elemento.get_text().strip()
                    if nome_produto and len(nome_produto) > 3:
                        break
            
            # Se não encontrou, tentar pelo title da página
            if not nome_produto:
                title_tag = soup.find('title')
                if title_tag:
                    title_text = title_tag.get_text().strip()
                    # Remover nome da loja do título
                    nome_produto = title_text.replace('Autocore Robótica', '').replace('|', '').strip()
            
            # Estratégias para encontrar preço
            preco_produto = None
            seletores_preco = [
                '.price-current',
                '.preco-atual',
                '.produto-preco',
                '.valor-produto', 
                '.price',
                '.preco',
                '.valor',
                '[class*="price"]',
                '[class*="preco"]',
                '[class*="valor"]'
            ]
            
            for seletor in seletores_preco:
                elemento = soup.select_one(seletor)
                if elemento:
                    texto_preco = elemento.get_text().strip()
                    if 'R$' in texto_preco:
                        preco_produto = texto_preco
                        break
            
            # Se não encontrou com seletores, buscar por padrão no texto
            if not preco_produto:
                texto_completo = soup.get_text()
                match_preco = re.search(r'R\$\s*\d+[,.]?\d*(?:[,.]?\d{2})?', texto_completo)
                if match_preco:
                    preco_produto = match_preco.group()
            
            # Validar dados encontrados
            if nome_produto and preco_produto:
                # Limpar nome do produto
                nome_limpo = re.sub(r'\s+', ' ', nome_produto).strip()
                nome_limpo = nome_limpo[:100]  # Limitar tamanho
                
                # Limpar preço
                preco_limpo = re.sub(r'[^\d,R$.]', ' ', preco_produto).strip()
                preco_limpo = re.sub(r'\s+', ' ', preco_limpo)
                
                return {
                    'produto': nome_limpo,
                    'preco': preco_limpo,
                    'url': url
                }
            
        except Exception as e:
            print(f"❌ Erro ao processar {url}: {e}")
        
        return None
    
    def extrair_com_selenium(self, urls_amostra):
        """Usa Selenium para sites mais complexos"""
        driver = self.get_driver()
        if not driver:
            return []
        
        produtos_selenium = []
        
        try:
            for i, url in enumerate(urls_amostra[:10]):  # Testar com 10 URLs
                print(f"🤖 Selenium processando {i+1}/10: {url}")
                
                try:
                    driver.get(url)
                    time.sleep(3)
                    
                    # Buscar nome do produto
                    nome = None
                    seletores_nome = ['h1', '.product-title', '.produto-titulo', '.nome-produto']
                    
                    for seletor in seletores_nome:
                        try:
                            elemento = driver.find_element(By.CSS_SELECTOR, seletor)
                            nome = elemento.text.strip()
                            if nome and len(nome) > 3:
                                break
                        except:
                            continue
                    
                    # Buscar preço
                    preco = None
                    elementos_preco = driver.find_elements(By.XPATH, "//*[contains(text(), 'R$')]")
                    
                    for elemento in elementos_preco:
                        texto = elemento.text.strip()
                        if re.match(r'R\$\s*\d+', texto):
                            preco = texto
                            break
                    
                    if nome and preco:
                        produtos_selenium.append({
                            'produto': nome[:100],  # Limitar tamanho
                            'preco': preco,
                            'url': url
                        })
                        print(f"   ✅ {nome} - {preco}")
                    else:
                        print(f"   ❌ Dados incompletos")
                        
                except Exception as e:
                    print(f"   ❌ Erro: {e}")
                
                time.sleep(2)  # Pausa entre produtos
                
        finally:
            driver.quit()
        
        return produtos_selenium
    
    def buscar_vitrine_principal(self):
        """Busca produtos na página principal/vitrine"""
        produtos_vitrine = []
        
        try:
            print("🏪 Buscando produtos na página principal...")
            response = requests.get(self.base_url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Buscar por cards/itens de produtos na vitrine
                seletores_vitrine = [
                    '.produto-item',
                    '.product-item',
                    '.card-produto',
                    '.item-produto',
                    '.vitrine-item',
                    '[class*="produto"]',
                    '[class*="product"]'
                ]
                
                for seletor in seletores_vitrine:
                    items = soup.select(seletor)
                    
                    if items:
                        print(f"   ✅ Encontrados {len(items)} itens com seletor: {seletor}")
                        
                        for item in items[:20]:  # Limitar a 20 por seletor
                            try:
                                # Buscar nome dentro do item
                                nome = None
                                for sel_nome in ['.nome', '.titulo', 'h3', 'h4', '.name', '.title']:
                                    elemento_nome = item.select_one(sel_nome)
                                    if elemento_nome:
                                        nome = elemento_nome.get_text().strip()
                                        break
                                
                                # Buscar preço dentro do item
                                preco = None
                                for sel_preco in ['.preco', '.price', '.valor']:
                                    elemento_preco = item.select_one(sel_preco)
                                    if elemento_preco:
                                        texto_preco = elemento_preco.get_text().strip()
                                        if 'R$' in texto_preco:
                                            preco = texto_preco
                                            break
                                
                                if nome and preco:
                                    produtos_vitrine.append({
                                        'produto': nome[:100],
                                        'preco': preco,
                                        'url': 'vitrine_principal'
                                    })
                            except:
                                continue
                        
                        if produtos_vitrine:
                            break  # Se encontrou produtos, não precisa testar outros seletores
                
        except Exception as e:
            print(f"❌ Erro na vitrine principal: {e}")
        
        return produtos_vitrine
    
    def executar_scraping_completo(self):
        """Executa o scraping focado em produtos individuais"""
        print("🛒 Iniciando extração de produtos individuais da Autocore...")
        
        todos_produtos = []
        
        # Estratégia 1: Buscar na vitrine principal
        produtos_vitrine = self.buscar_vitrine_principal()
        if produtos_vitrine:
            print(f"✅ Vitrine: {len(produtos_vitrine)} produtos")
            todos_produtos.extend(produtos_vitrine)
        
        # Estratégia 2: Buscar URLs de produtos específicos
        urls_produtos = self.obter_urls_produtos()
        
        if urls_produtos:
            print(f"\n🔗 Processando {len(urls_produtos)} URLs de produtos...")
            
            for i, url in enumerate(urls_produtos[:20]):  # Limitar para teste
                print(f"   📦 {i+1}/{min(20, len(urls_produtos))}: {url}")
                produto = self.extrair_produto_individual(url)
                
                if produto:
                    todos_produtos.append(produto)
                    print(f"      ✅ {produto['produto']} - {produto['preco']}")
                else:
                    print(f"      ❌ Sem dados")
                
                time.sleep(1)  # Pausa respeitosa
        
        # Estratégia 3: Se ainda não tem muitos produtos, tentar Selenium
        if len(todos_produtos) < 10:
            print(f"\n🤖 Poucos produtos encontrados ({len(todos_produtos)}). Tentando Selenium...")
            produtos_selenium = self.extrair_com_selenium(urls_produtos[:10])
            todos_produtos.extend(produtos_selenium)
        
        return todos_produtos
    
    def processar_e_salvar(self, produtos_brutos):
        """Processa e salva os dados finais"""
        if not produtos_brutos:
            print("❌ Nenhum produto coletado!")
            return None
        
        # Criar DataFrame
        df = pd.DataFrame(produtos_brutos)
        
        # Remover duplicatas baseado no nome
        df = df.drop_duplicates(subset=['produto'], keep='first')
        
        # Limpar dados
        df['produto'] = df['produto'].str.strip()
        df['produto'] = df['produto'].str.replace(r'\s+', ' ', regex=True)
        
        # Padronizar preços
        def padronizar_preco(preco):
            if pd.isna(preco):
                return preco
            
            # Extrair apenas números e vírgulas/pontos
            match = re.search(r'R\$?\s*(\d+[,.]\d{2}|\d+)', str(preco))
            if match:
                valor = match.group(1)
                return f"R$ {valor}"
            return preco
        
        df['preco'] = df['preco'].apply(padronizar_preco)
        
        # Filtrar produtos válidos
        df = df[df['produto'].str.len() > 2]
        df = df[df['preco'].str.contains('R\$', na=False)]
        
        # Remover coluna URL se não for necessária
        if 'url' in df.columns:
            df = df[['produto', 'preco']]
        
        # Renomear colunas para ficar mais claro
        df.columns = ['Produto', 'Preço']
        
        # Salvar
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        csv_file = f'autocore_produtos_individuais_{timestamp}.csv'
        excel_file = f'autocore_produtos_individuais_{timestamp}.xlsx'
        
        try:
            df.to_csv(csv_file, index=False, encoding='utf-8-sig')
            print(f"✅ CSV salvo: {csv_file}")
        except Exception as e:
            print(f"❌ Erro CSV: {e}")
        
        try:
            df.to_excel(excel_file, index=False)
            print(f"✅ Excel salvo: {excel_file}")
        except Exception as e:
            print(f"❌ Erro Excel: {e}")
        
        return df
    
    def executar(self):
        """Método principal"""
        try:
            produtos = self.executar_scraping_completo()
            
            print(f"\n📊 Produtos coletados: {len(produtos)}")
            
            if produtos:
                # Mostrar amostra
                print("\n🎯 Amostra dos produtos encontrados:")
                for i, produto in enumerate(produtos[:10]):
                    print(f"   {i+1}. {produto['produto']} - {produto['preco']}")
                
                # Processar e salvar
                df_final = self.processar_e_salvar(produtos)
                
                if df_final is not None:
                    print(f"\n🎉 Sucesso! {len(df_final)} produtos únicos salvos.")
                    print("\n📋 Resumo da tabela:")
                    print(df_final.head(10).to_string(index=False))
                    return df_final
            
            print("\n❌ Nenhum produto individual foi encontrado.")
            return None
            
        except Exception as e:
            print(f"❌ Erro geral: {e}")
            return None

def main():
    scraper = AutocoreScraperProdutos()
    resultado = scraper.executar()
    
    if resultado is not None:
        print(f"\n✅ Scraping concluído! Tabela com {len(resultado)} produtos.")
    else:
        print("\n❌ Scraping não encontrou produtos individuais.")

if __name__ == "__main__":
    main()