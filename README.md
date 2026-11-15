# Rotas alternativas na Grande Natal

Compare links para trajetos com paradas diferentes e abra cada opção no Google Maps.

## Rodar

Python 3.10 ou mais recente. Cada execução lê um JSON local e imprime outro JSON no terminal.

```bash
python app.py exemplo.json
python -m unittest -v
```

## Uso

Cada alternativa pode ter até três paradas nomeadas, na ordem de passagem. Escolha o modo `carro`, `a-pe`, `bicicleta` ou `onibus`. O Google Maps permite usar a preferência de evitar pedágios onde aplicável.

## Google Maps

Os links seguem a documentação de [Maps URLs](https://developers.google.com/maps/documentation/urls/get-started) e abrem o app ou site sem chave. Confira no Maps a rota oferecida, a cobertura de transporte e as condições do momento. Os valores numéricos no arquivo de exemplo são demonstrações.

## Estado do projeto

Versão inicial funcional por linha de comando, sem interface web. Usa apenas a biblioteca padrão do Python. Os testes executam os exemplos e verificam as regras do projeto.
