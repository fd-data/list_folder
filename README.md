# Listador de Diretório

Esta aplicação em Python, construída com a biblioteca Streamlit, permite listar todos os arquivos e pastas em um diretório especificado pelo usuário, incluindo seus tamanhos (em bytes, MB, e GB) e datas de modificação. Além disso, a ferramenta oferece opções para exportar esses dados em formatos CSV e TXT.

## Funcionalidades

- Lista arquivos e pastas de um diretório especificado, exibindo seus tamanhos e datas de modificação.
- Exporta a lista gerada para os formatos CSV e TXT.
- Oferece uma barra de progresso durante o processamento para informar o andamento ao usuário.
- Permite reiniciar a aplicação com um botão dedicado.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema, junto com as seguintes bibliotecas:

- `streamlit`
- `pandas`
- `tabulate`

Você pode instalá-las utilizando o pip:

```bash
pip install streamlit pandas tabulate

