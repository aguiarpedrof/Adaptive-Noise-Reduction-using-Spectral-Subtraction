# Filtro de Ruído Adaptativo via Subtração Espectral / Adaptive Noise Reduction

## 🇧🇷 Português

### Justificativa Técnica
A remoção de ruído branco de banda larga não pode ser realizada de forma eficiente via filtros LTI (Lineares e Invariantes no Tempo) convencionais, como filtros Passa-Baixa. Como o ruído branco possui densidade espectral de potência constante em todo o espectro, um filtro passa-baixa causaria perda severa de harmônicos do sinal de interesse sem remover o ruído nas bandas passantes.

Este projeto utiliza a **Subtração Espectral** no domínio da frequência para estimar e atenuar o ruído sem comprometer a largura de banda do sinal original.

### Problemas de Implementação e Decisões de Projeto
1. **Janelamento e Vazamento Espectral:** Utilizou-se a **STFT** com janela de **Hamming** para reduzir descontinuidades nas bordas dos frames, minimizando o espalhamento de energia (*spectral leakage*).
2. **Preservação de Fase:** A fase original do sinal é preservada e recombinada à magnitude processada antes da **ISTFT**, garantindo a integridade temporal do áudio.
3. **Musical Noise e Thresholding:** Para mitigar artefatos metálicos, implementou-se um **Over-subtraction Factor** e um **Noise Floor** (piso de ruído), evitando vácuos espectrais artificiais.

---

## 🇺🇸 English

### Technical Rationale
Wideband white noise removal cannot be efficiently performed via conventional LTI (Linear Time-Invariant) filters, such as Low-Pass filters. Since white noise has a constant power spectral density across the spectrum, a low-pass filter would cause severe loss of signal harmonics without removing noise in the passbands.

This project employs **Spectral Subtraction** in the frequency domain to estimate and attenuate noise without compromising the original signal's bandwidth.

### Implementation Issues & Design Decisions
1. **Windowing & Spectral Leakage:** **STFT** with a **Hamming** window was used to reduce discontinuities at frame boundaries, minimizing energy spreading (*spectral leakage*).
2. **Phase Preservation:** The original signal phase is preserved and recombined with the processed magnitude before **ISTFT**, ensuring the temporal integrity of the audio.
3. **Musical Noise & Thresholding:** To mitigate metallic artifacts, an **Over-subtraction Factor** and a **Noise Floor** were implemented, avoiding artificial spectral voids.

---

## 📊 Métricas / Metrics
- **SNR (Signal-to-Noise Ratio)** calculation included to quantify decibel (dB) gain.
- **Visual Validation:** Time-domain plots and Spectrograms.

## 🚀 Como Executar / How to Run
```bash
pip install numpy scipy matplotlib
python demo.py