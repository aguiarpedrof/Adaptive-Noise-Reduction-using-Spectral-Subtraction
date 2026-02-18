import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

def calculate_snr(reference, noisy):
    
    min_len = min(len(reference), len(noisy))
    ref = reference[:min_len]
    nos = noisy[:min_len]
    
    signal_power = np.mean(ref**2)
    noise_power = np.mean((ref - nos)**2)
    return 10 * np.log10(signal_power / noise_power)

# --- CONFIGURAÇÕES ---
fs = 44100
duration = 1.0
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

clean_signal = 0.5 * np.sin(2 * np.pi * 440 * t)
white_noise = np.random.normal(0, 0.08, len(t))
noisy_signal = clean_signal + white_noise

f, t_spec, Zxx = signal.stft(noisy_signal, fs, nperseg=1024)
magnitude = np.abs(Zxx)
phase = np.angle(Zxx)

noise_profile = np.mean(magnitude[:, :15], axis=1, keepdims=True)

magnitude_clean = magnitude - (1.5 * noise_profile)
magnitude_clean = np.maximum(magnitude_clean, 0.02 * magnitude)

Zxx_clean = magnitude_clean * np.exp(1j * phase)
_, filtered_signal = signal.istft(Zxx_clean, fs)

filtered_signal = filtered_signal[:len(clean_signal)]

snr_before = calculate_snr(clean_signal, noisy_signal)
snr_after = calculate_snr(clean_signal, filtered_signal)

print(f"📊 Relatório de Performance:")
print(f"   SNR Inicial: {snr_before:.2f} dB")
print(f"   SNR Final:   {snr_after:.2f} dB")
print(f"   Melhoria:    {snr_after - snr_before:.2f} dB")

plt.style.use('seaborn-v0_8-darkgrid') 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), dpi=100)

ax1.plot(t, noisy_signal, color='#ff7f0e', alpha=0.5, label='Noisy Signal')
ax1.plot(t, filtered_signal, color='#1f77b4', label='Filtered Signal', linewidth=1.5)
ax1.set_xlim(0, 0.02)
ax1.set_title("Time Domain Analysis (First 20ms)")
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Amplitude")
ax1.legend()

im = ax2.specgram(filtered_signal, Fs=fs, NFFT=1024, cmap='viridis')
ax2.set_title("Spectrogram After Filtering")
ax2.set_ylabel("Frequency [Hz]")
ax2.set_xlabel("Time [s]")
ax2.set_ylim(0, 2000)

plt.tight_layout()
plt.savefig('comparison_result.png') 
plt.show()
wavfile.write("filtered_output.wav", fs, filtered_signal.astype(np.float32))