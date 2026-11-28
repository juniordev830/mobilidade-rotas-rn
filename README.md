# Rotas alternativas na Grande Natal

**Navegação** · [Rodar](#rodar) · [Uso](#uso) · [Google Maps](#google-maps) · [Código e estudo](docs/ENGENHARIA_REVERSA.md)

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

Também é possível encadear a ferramenta com outro comando usando `-` como entrada. Exemplo em um terminal Bash:

```bash
cat exemplo.json | python app.py -
```

As alternativas devem ter nomes distintos (ignorando maiúsculas/minúsculas e espaços nas bordas). O programa aceita de 1 a 25 opções por consulta e preserva a ordem informada.

Arquivos e entrada padrão JSON são limitados a 1 MB (1.000.000 bytes). Entradas maiores são rejeitadas antes da decodificação e da geração de URLs.

## Código e roteiro de estudo

Qual é a diferença entre construir um link com paradas e calcular a duração de um trajeto? O [guia de engenharia reversa](docs/ENGENHARIA_REVERSA.md) reúne o mapa dos módulos e uma pergunta técnica baseada no projeto.

Mantido por [João Junior](https://github.com/juniordev830).
