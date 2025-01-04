m = float(input('Digite um valor em metros: '))
print(f'''A medida de \033[1;36m{m}m\033[m corresponde a
\033[1;34m{m / 1000}\033[mKm
\033[1;34m{m / 100}\033[mHm
\033[1;34m{m / 10}\033[mDam
\033[1;34m{m * 10:.0f}\033[mDm
\033[1;34m{m * 10:.0f}\033[mCm
\033[1;34m{m * 1000:.0f}\033[mMm''')