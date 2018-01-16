N = 20
frequency_space = 2000000

rx_freq_list = [2400000000.0 + i * frequency_space for i in range(N)]
tx_freq_list = [0 for i in range(N)]
for i in range(N-1):
    tx_freq_list[i] = rx_freq_list[i+1]
tx_freq_list[N-1] = rx_freq_list[0]

print tx_freq_list
print rx_freq_list
