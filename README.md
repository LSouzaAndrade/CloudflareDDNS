# CloudflareDDNS
Este projeto é um sideproject desenvolvido para gerenciar a operação da minha VPS com IP dinâmico. O script [`update_ip.py`](./scripts/update_ip.py) é configurado para ser executado periodicamente via cron, verificando se houve alteração no endereço IP da rede onde a VPS está conectada. Caso uma mudança seja detectada, o script utiliza a API do Cloudflare para atualizar o registro DNS do domínio usado para conexão SSH com a VPS.

## Estrutura do projeto
```
├── data/                   # Diretório de permanência de dados
│   ├── ip.txt              # Arquivo para permanência do IP anterior
│   └── records_info.txt    # Arquivo contendo informações dos records do domínio
├── ddns/                   # Módulo principal com funções
│   ├── __init__.py         # Inicializador do módulo Python 'ddns'
│   ├── cloudflare_api.py   # Função para interação com a API do Cloudflare
│   ├── ip_manager.py       # Funções para obtenção e armazenamento do IP anterior
│   ├── ip_service.py       # Função para obtenção do IP atual
│   └── logger.py           # Parametrização de logging de informações no terminal
├── scripts/                # Scripts executáveis
│   ├── get_record_id.txt   # Script auxiliar para obter o record ID do domínio na CloudFlare
│   └── update_ip.py        # Script principal que executa o processo (entrypoint)
├── example.env             # Arquivo template para variáveis de ambiente (renomeie para .env)
├── .python-version         # Versão do Python utilizada no projeto
├── LICENSE                 # Arquivo de licença do projeto
├── pyproject.toml          # Configurações do projeto e dependências
├── README.md               # Documentação do projeto
└── uv.lock                 # Arquivo de lock de dependências do UV
```
