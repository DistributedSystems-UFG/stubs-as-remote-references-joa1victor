# Stubs como Referências Remotas

Este repositório contém a implementação do exemplo da Nota 4.8 do livro Tanenbaum & Van Steen (2025), que demonstra o uso de stubs como referências remotas em sistemas distribuídos.

## Como executar

### Local
```bash
python3 run.py
```

### AWS (3 máquinas)

No SERVER:
```bash
python3 server.py
```

No PEER2:
```bash
python3 client2aws.py
```

No PEER1:
```bash
python3 client1aws.py
```

## Arquivos

- `server.py` — servidor de listas
- `dbclient.py` — stub que representa a referência remota
- `client.py` — classe de comunicação entre clientes
- `constRPC.py` — constantes e endereços das máquinas
- `run.py` — execução local com multiprocessing
- `client1aws.py` — client1 para execução na AWS
- `client2aws.py` — client2 para execução na AWS
