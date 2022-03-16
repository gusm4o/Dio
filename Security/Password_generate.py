import random, string
tam = 16

chars = string.ascii_letters + string.digits + '!@#$%*()_+/*-+.<:>|'

rnd = random.SystemRandom() ##os.urandoom

print(''.join(rnd.choice(chars)for i in range(tam)))