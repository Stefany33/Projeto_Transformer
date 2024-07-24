from scipy.stats import binom
import streamlit as st

def calcular_ITM(n, Pa, N):
    return n + (1 - Pa) * (N - n)

def calcular_riscos_e_custos(N, custo_unitario_inspecao, despesa_lote_reprovado, NQA, n, a, taxa_defeituosos, dias_uteis_mes, PTDL):
    # Cálculo dos riscos
    risco_fornecedor = 1 - binom.cdf(a, n, NQA / 100)
    risco_consumidor = binom.cdf(a, n, PTDL / 100)

    # Cálculo da probabilidade de aceitação considerando a taxa de defeitos atual
    Pa = binom.cdf(a, n, taxa_defeituosos / 100)

    # Cálculo da Inspeção Total Média (ITM) considerando a taxa de defeitos atual
    ITM = calcular_ITM(n, Pa, N)

    # Cálculo dos custos de inspeção
    custo_inspecao = dias_uteis_mes * ITM * custo_unitario_inspecao
    custo_lotes_rejeitados = dias_uteis_mes * (1 - Pa) * despesa_lote_reprovado

    # Cálculo do custo total considerando lotes reprovados
    custo_total = custo_inspecao + custo_lotes_rejeitados

    # Determinação de aceitação ou rejeição do lote
    lote_aceito = Pa > (1 - PTDL / 100)

    # Resultados
    return risco_fornecedor, risco_consumidor, custo_inspecao, custo_total, ITM, custo_lotes_rejeitados, lote_aceito

# Função principal para entrada de dados e chamada dos cálculos
def main():
    st.title('Plano Amostral')

    # Entradas dos parâmetros
    N = st.number_input('Tamanho do lote (N):', min_value=1, value=10000, step=1)
    dias_uteis_mes = st.number_input('Número de dias úteis no mês:', min_value=1, value=20, step=1)
    custo_unitario_inspecao = st.number_input('Custo unitário de inspeção: R$', min_value=0.0, value=1.0, step=0.01, format="%.2f")
    despesa_lote_reprovado = st.number_input('Despesa por lote reprovado: R$', min_value=0.0, value=500.0, step=1.0, format="%.2f")
    NQA = st.number_input('Nível de Qualidade Aceitável (NQA) em %:', min_value=0.0, value=0.02, step=0.01, format="%.3f")
    n = st.number_input('Tamanho da amostra (n):', min_value=1, value=100, step=1)
    a = st.number_input('Índice de aceitação máxima (a):', min_value=0, value=5, step=1)
    taxa_defeituosos = st.number_input('Histórico da taxa de defeituosos do fornecedor em %:', min_value=0.0, value=0.05, step=0.01, format="%.3f")
    PTDL = st.number_input('Percentual Tolerável de Defeitos no Lote (PTDL) em %:', min_value=0.0, value=0.04, step=0.01, format="%.3f")

    if st.button('Calcular'):
        risco_fornecedor, risco_consumidor, custo_inspecao, custo_total, ITM, custo_lotes_rejeitados, lote_aceito = calcular_riscos_e_custos(
            N, custo_unitario_inspecao, despesa_lote_reprovado, NQA, n, a, taxa_defeituosos, dias_uteis_mes, PTDL
        )

        # Exibição dos resultados
        st.write('Resultados:')
        st.write(f'Risco do fornecedor: {risco_fornecedor:.4f}')
        st.write(f'Risco do consumidor: {risco_consumidor:.4f}')
        st.write(f'Custo de inspeção: R$ {custo_inspecao:.2f}')
        st.write(f'Custo de despesas: R$ {custo_lotes_rejeitados:.2f}')
        st.write(f'Custo total: R$ {custo_total:.2f}')
        st.write(f'Inspeção Total Média (ITM): {ITM:.2f}')
        st.write(f'Lote aceito? {"Sim" if lote_aceito else "Não"}')

if __name__ == "__main__":
    main()
