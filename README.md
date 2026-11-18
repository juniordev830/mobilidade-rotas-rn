# Rotas alternativas na Grande Natal

Compare links para trajetos com paradas diferentes e abra cada opção no Google Maps.

## Rodar

Python 3.10 ou mais recente. Cada execução lê um JSON local e imprime outro JSON no terminal.

```bash
python app.py exemplo.json
python -m unittest -v
```

## Uso

Cada alternativa pode ter até três paradas nomeadas, na ordem de passagem. Escolha o modo padrão `carro`, `a-pe`, `bicicleta` ou `onibus` em `modo`. Para comparar meios de transporte no mesmo relatório, informe `modo` em uma alternativa; as demais continuam usando o modo padrão. Um modo desconhecido é rejeitado. O Google Maps permite usar a preferência de evitar pedágios onde aplicável.

```json
{
  "origem": "Natal, RN",
  "destino": "Parnamirim, RN",
  "modo": "carro",
  "alternativas": [
    {"nome": "Pedal", "modo": "bicicleta", "paradas": []},
    {"nome": "Carro", "paradas": []}
  ]
}
```

## Google Maps

Os links seguem a documentação de [Maps URLs](https://developers.google.com/maps/documentation/urls/get-started) e abrem o app ou site sem chave. Confira no Maps a rota oferecida, a cobertura de transporte e as condições do momento. Os valores numéricos no arquivo de exemplo são demonstrações.

## Estado do projeto

Versão inicial funcional por linha de comando, sem interface web. Usa apenas a biblioteca padrão do Python. Os testes executam os exemplos e verificam as regras do projeto.

## Exportação para planilha

Use `python app.py exemplo.json --csv > relatorio.csv` para exportar as alternativas de rota com seus links. O CSV usa ponto e vírgula, conserva a ordem do relatório e inclui o cabeçalho mesmo quando a seleção está vazia. O JSON continua sendo a saída padrão.
