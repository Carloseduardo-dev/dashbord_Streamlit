# 📊 Dashboard ESC Engenharia

Este projeto é um **dashboard interativo** desenvolvido com [Streamlit](https://streamlit.io/) para **visualização e análise de dados** da empresa **ESC Engenharia**.

## 🔧 Funcionalidades

* 📋 Exibição de tabela de dados com índice ajustado
* 📈 Estatísticas descritivas da coluna `Quantidade`
* 🎛️ Filtros interativos por tipo de projeto
* 📊 Visualizações gráficas:

  * Gráfico de **barras** por tipo de projeto
  * **Histograma** com curva KDE da coluna `Quantidade`
  * Gráfico de **dispersão** com linha de regressão

## 📁 Estrutura dos Arquivos

* `projeto_streamlit_dashbord.py`: Script principal da aplicação Streamlit
* `esc_engenharia.csv`: Arquivo CSV com os dados (deve estar no mesmo diretório)
* `README.md`: Este arquivo

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3.8+** instalado.
2. Instale as dependências necessárias:

   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```
3. No terminal, execute o projeto com:

   ```bash
   streamlit run projeto_streamlit_dashbord.py
   ```

## 🌐 Fonte dos Dados

Os dados utilizados pertencem à empresa **ESC Engenharia**.
Mais informações: [http://www.esc.com.br](http://www.esc.com.br)
