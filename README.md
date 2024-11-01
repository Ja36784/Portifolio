# Portfólio Pessoal de José Azarias

Este é o código-fonte do meu portfólio pessoal, desenvolvido com HTML, CSS e Bootstrap. O site apresenta minhas habilidades, experiência, projetos e contato.

## 🖥️ Tecnologias Utilizadas

- **HTML**: Estrutura da página
- **CSS**: Estilos e layout
- **Bootstrap**: Design responsivo e ícones
- **JavaScript**: Funcionalidades e interatividade
- **Python (Flask)**: Backend para o formulário de contato (se aplicável)
- **Flask-Mail**
- **Phyton**
- **Dotenv (para gerenciamento de variáveis de ambiente)**

## Requisitos
- Para executar este projeto, você precisará ter o Python 3 e o pip instalados. Além disso, você deve instalar as seguintes bibliotecas:

```bash
pip install Flask Flask-Mail python-dotenv
 

## 📄 Estrutura do Projeto

📁 static │ ├── css │ │ └── style.css # Estilos customizados │ ├── img │ │ ├── 8.jpg # Ícone do site │ │ └── outras imagens # Imagens usadas no site │ └── bootstrap │ └── css/bootstrap.css # Biblioteca Bootstrap ├── templates │ └── index.html # Página principal └── app.py # Servidor Flask (se aplicável)

markdown
Copy code

/seu_projeto
│
├── app.py             # Arquivo principal do aplicativo
├── templates
│   └── index.html     # Template HTML para o formulário de contato
├── .env               # Variáveis de ambiente (não deve ser compartilhado)
└── requirements.txt    # Lista de dependências


## 🖼️ Visão Geral do Conteúdo

### Sessões Principais

1. **Início**: Introdução com nome e título.
2. **Sobre**: Informações pessoais e apresentação.
3. **Habilidades**: Competências técnicas e pessoais com barra de progresso.
4. **Currículo**: Histórico profissional e acadêmico.
5. **Contato**: Formulário de contato com integração Flask para envio (se configurado).

**Como Usar**
1. Acesse o aplicativo em seu navegador.
2. Preencha o formulário de contato com seu nome, e-mail e mensagem.
3. Clique em "Enviar". Uma mensagem de confirmação será exibida se o e-mail for enviado com sucesso.

**Detalhes do Código**
* Flask: Usado para criar o servidor web e gerenciar rotas.
* Flask-Mail: Usado para enviar e-mails. As configurações de e-mail são carregadas a partir do arquivo .env.
dotenv: Utilizado para gerenciar variáveis de ambiente sensíveis.
* Classe Contato: Representa as informações do formulário de contato com atributos para nome, e-mail e mensagem.

**Contribuições**
Sinta-se à vontade para fazer contribuições, sugestões ou relatar problemas.

