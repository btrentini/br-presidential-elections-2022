# Cria um arquivo para salvar os links que vamos baixar
touch resources/download_logs.sh

# Executa o script para encontrar os links de logs das urnas no site do TSE
python src/datafind.py

# Baixa os arquivos do TSE um por um
sh ./resources/download_logs.sh 
