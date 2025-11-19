# Assistente de Estudos IA (Projeto - Nível Iniciante)

Projeto de exemplo: Assistente de Estudos que usa LLMs e aplica práticas básicas de LLMOps.
Esta versão é intencionalmente simples para você entender e aprender os conceitos.

## Estrutura do projeto
```
assistente-estudos-ia/
│── app.py                  # backend Python/Flask
│── prompt_v1.txt           # versão 1 do prompt (LLMOps: versionamento)
│── prompt_v2.txt
│── prompt_v3.txt
│── logs/
│      └── interactions.json   # logs das conversas (LLMOps)
│── templates/
│      └── index.html          # interface do usuário
│── static/
│      └── style.css
└── README.md
```

## O que é LLMOps neste projeto?
- **Versionamento de prompts**: cada arquivo `prompt_v*.txt` representa uma versão do prompt. Alterar o prompt e salvar como nova versão permite testar melhorias com segurança.
- **Logs de interação**: `logs/interactions.json` armazena cada pergunta e resposta para análise posterior (qualidade, erros, custos).
- **Melhoria contínua**: você pode ajustar prompts, testar e comparar resultados com logs anteriores.

## Requisitos
- Python 3.10+
- (Opcional) Conta e chave de API OpenAI ou equivalente para rodar com modelo real.
- Dependências (recomendado criar virtualenv):
```
pip install flask openai
```

## Como rodar localmente (modo mock sem API)
1. Clone este diretório ou copie os arquivos.
2. Crie um virtualenv (opcional):
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows (PowerShell)
```
3. Instale dependências mínimas (Flask):
```
pip install flask
```
4. Rode a aplicação (modo mock, sem chave):
```
python app.py
```
Acesse http://localhost:5000 e teste o Assistente. As respostas serão mockadas se não houver chave de API.

## Como rodar com OpenAI (ou outro provedor compatível)
1. Instale dependência OpenAI (se usar):
```
pip install openai
```
2. Configure variável de ambiente:
```
export OPENAI_API_KEY="sua_chave"
# ou no Windows (PowerShell):
# setx OPENAI_API_KEY "sua_chave"
```
3. Rode:
```
python app.py
```
O backend tentará usar a API se a chave estiver disponível.

## Como testar LLMOps (passos práticos)
1. Rode o servidor e faça perguntas pela interface.
2. Verifique `logs/interactions.json` para ver as perguntas/respostas.
3. Crie `prompt_v4.txt` com ajustes (ex.: mais concisão) e salve.
4. Faça novas perguntas e compare respostas entre versões (observe melhorias).
5. Edite README.md com observações e prints do processo. Isso conta como documentação LLMOps.

## Notas finais / como usar este projeto no currículo
- No seu currículo, descreva o projeto como: *"Assistente Inteligente de Estudos — integração com LLM via API, versionamento de prompts (LLMOps iniciante), logs de interações e prototipação."*
- Este projeto demonstra compreensão prática do fluxo de LLMOps, mesmo em nível inicial.

---
Se quiser, eu **posso** também:
- criar um arquivo requirements.txt
- empacotar o projeto em um zip para download
- gerar um README mais curto para colocar no GitHub
- criar um deploy simples (ex: instruções para Render/Vercel)

Qual desses você quer agora?
(1) Zip do projeto para baixar
(2) requirements.txt
(3) Deploy instructions para Render
(4) Tudo acima
# assistente-de-estudos-ia
# assistente-de-estudos-ia
