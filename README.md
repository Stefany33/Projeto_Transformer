# Integrantes do Grupo:
    -Ana Beatriz Souto Pereira - 802357
    -Lucas Bianchin P. de Albuquerque - 802805
    -Nathalia Yuki Enokida - 802230
    -Stefany Takahashi - 801482

# Documentação para o Código de Plano Amostral

    Este projeto implementa uma ferramenta interativa para a análise de risco e custo em um plano amostral. A ferramenta é desenvolvida em Python, utilizando as bibliotecas scipy.stats e streamlit, e permite calcular o risco do fornecedor e do consumidor, além de estimar custos de inspeção e rejeição de lotes com base em parâmetros fornecidos pelo usuário.

    O objetivo é fornecer uma interface simples para realizar simulações e análises de planos amostrais, facilitando a tomada de decisões na inspeção de qualidade de lotes de produção.

# Funções:

# calcular_ITM(n, Pa, N)
    
    Calcula a Inspeção Total Média (ITM) com base no tamanho da amostra (n), a probabilidade de aceitação (Pa), e o tamanho do lote (N).

# calcular_riscos_e_custos(...)
    
    Calcula os riscos e custos de inspeção e reprovação do lote. Retorna os seguintes resultados:

        Risco do fornecedor: A probabilidade de o fornecedor ter seu lote rejeitado mesmo quando o lote atende ao NQA.

        Risco do consumidor: A probabilidade de o consumidor aceitar um lote que excede o PTDL.

        Custo de inspeção: O custo total da inspeção ao longo dos dias úteis do mês.

        Custo total: A soma do custo de inspeção e das despesas com lotes reprovados.
        
        ITM: O valor médio de inspeções realizadas.
        
        Despesas com lotes reprovados: O custo devido à rejeição de lotes.
        
        Lote aceito: Retorna se o lote foi aceito ou não com base no percentual de defeitos e nas tolerâncias fornecidas.
        
# main()
    
    Esta é a função principal que cria a interface do usuário utilizando o Streamlit. Ela coleta os parâmetros de entrada e chama a função calcular_riscos_e_custos() para realizar os cálculos.

# Parâmetros de Entrada:
    
    Tamanho do lote (N): O número total de unidades no lote a ser inspecionado.
    
    Dias úteis no mês: O número de dias úteis no mês, usado para estimar o custo total da inspeção.
    
    Custo unitário de inspeção: O custo de inspecionar uma unidade.
    
    Despesa por lote reprovado: O custo quando um lote é rejeitado.
    
    Nível de Qualidade Aceitável (NQA): Percentual máximo de defeitos permitidos no lote para ser considerado aceitável.
    
    Tamanho da amostra (n): O número de unidades a serem inspecionadas.
    
    Índice de aceitação máxima (a): O número máximo de unidades defeituosas permitido na amostra.
    
    Histórico da taxa de defeituosos do fornecedor: Percentual de defeitos baseado no histórico do 
    fornecedor.
    
    Percentual Tolerável de Defeitos no Lote (PTDL): O percentual máximo de defeitos tolerável para o lote.
    
# Resultados Exibidos:

    Risco do fornecedor: A probabilidade de rejeitar um lote dentro da qualidade aceitável.

    Risco do consumidor: A probabilidade de aceitar um lote com defeitos acima do limite tolerável.

    Custo de inspeção: O valor total gasto com inspeções.
    
    Custo de despesas: O valor associado aos lotes rejeitados.
    
    Custo total: A soma dos custos de inspeção e das despesas.
    
    Inspeção Total Média (ITM): O número médio de inspeções realizadas.

    Lote aceito: Um indicador de se o lote foi aceito ou rejeitado com base na amostragem.

# Criação do requirements.txt:

    O arquivo requirements.txt é utilizado para listar todas as bibliotecas e dependências necessárias para rodar o projeto Python. Ele é importante para garantir que o projeto funcione em qualquer ambiente, instalando as mesmas versões dos pacotes usados no desenvolvimento.

        pip freeze > requirements.txt
        pip install -r requirements.txt

    Isso garante que todas as bibliotecas necessárias, com as versões corretas, sejam instaladas para rodar o projeto corretamente.

# Controle de Versão com Git e Upload no GitHub

    Durante o desenvolvimento, foi utilizado o sistema de controle de versão Git para gerenciar as alterações no código. O Git foi utilizado para rastrear as modificações no projeto e fazer a atualização dos arquivos.

# Passos para uso do Git:

    Inicie o repositório Git no diretório do projeto:

        git init

    Adicione os arquivos ao controle de versão:

        git add .

    Faça o commit das alterações:

        git commit -m "..."

    Suba o código para o GitHub:

        git remote set-url origin https://Stefany33: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@github.com/Stefany33/Projeto_Transformer.git

        git push -u origin master

# Criação do Aplicativo com Streamlit:

     projeto foi transformado em um aplicativo web utilizando o Streamlit, uma plataforma que permite a construção de dashboards e aplicações interativas de forma rápida e intuitiva.

# Passos para publicar o aplicativo:
        
    Acesse o site Streamlit.

    Vincule sua conta do GitHub ao Streamlit para permitir a importação do código do repositório.

    No Streamlit, selecione o repositório do GitHub onde o código do projeto está hospedado e siga os passos para configurar o aplicativo.

    Após a configuração, o aplicativo será publicado e um link será gerado para acessá-lo publicamente.

