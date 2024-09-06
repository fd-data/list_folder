import os
import time
import streamlit as st
import pandas as pd
from tabulate import tabulate

def convert_size(size_bytes):
    """Convert size from bytes to MB and GB."""
    mb = size_bytes / (1024 * 1024)
    gb = size_bytes / (1024 * 1024 * 1024)
    return mb, gb

def get_folder_size(directory):
    """Calculate the total size of the directory, including all subdirectories and files."""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                file_path = os.path.join(root, name)
                total_size += os.path.getsize(file_path)
            except PermissionError:
                continue
    return total_size

def list_files_and_folders(directory):
    """List files and folders with their sizes and modification dates."""
    items = []

    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_file():
                path = entry.path
                size_bytes = entry.stat().st_size
                mb, gb = convert_size(size_bytes)
                mod_time = entry.stat().st_mtime
                mod_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
                items.append((path, size_bytes, mb, gb, mod_date))
                
            elif entry.is_dir():
                path = entry.path
                size_bytes = get_folder_size(path)
                mb, gb = convert_size(size_bytes)
                mod_time = entry.stat().st_mtime
                mod_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
                items.append((path, size_bytes, mb, gb, mod_date))

    # Sort items by size in descending order
    items.sort(key=lambda x: x[1], reverse=True)
    
    # Prepare data for DataFrame
    df = pd.DataFrame(items, columns=["Caminho", "Tamanho (Bytes)", "Tamanho (MB)", "Tamanho (GB)", "Data de Modificação"])
    return df

def main():
    st.title("Listador de Diretório")
    st.write("Esta ferramenta lista todos os arquivos e pastas em um diretório especificado, incluindo seus tamanhos e datas de modificação.")

    # Input for directory
    directory = st.text_input("Diretório a ser listado:", "")
    if st.button("Listar Arquivos e Pastas"):
        if directory and os.path.exists(directory):
            with st.spinner('Processando...'):

                # Process the files and update the progress bar 
                df = list_files_and_folders(directory)
                st.success("Processamento concluído!")
                st.write("## Resultados")
                st.dataframe(df)

                # Export options side by side
                st.write("### Exportar Resultados")
                col1, col2, col3, col4, col5, col6 = st.columns(6)

                with col1:
                    # Export to CSV
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Baixar CSV",
                        data=csv,
                        file_name='lista_arquivos.csv',
                        mime='text/csv',
                    )

                with col2:
                    # Export to TXT
                    txt = tabulate(df, headers='keys', tablefmt='grid')
                    st.download_button(
                        label="Baixar TXT",
                        data=txt.encode('utf-8'),
                        file_name='lista_arquivos.txt',
                        mime='text/plain',
                    )
                
                with col6:
                    # Add a "Reiniciar" button to reload the page
                    st.write("###")
                    if st.button("Reiniciar"):
                        st.experimental_rerun()

        else:
            st.error("Por favor, insira um diretório válido.")

if __name__ == "__main__":
    main()
