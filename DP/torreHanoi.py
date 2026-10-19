from math import sqrt

def eh_quadrado(x: int) -> bool:
   r = int(sqrt(x))
   return pow(r, 2) == x

def torre_de_hanoi_matrix(qtdd_hastes: int) -> int:
   hastes = [[] for _ in range(qtdd_hastes)]
   is_empty = lambda x: len(x) == 0

   bola = 1
   while True:
      colocado = False
      for i in range(qtdd_hastes):
         if is_empty(hastes[i]) or eh_quadrado(bola + hastes[i][-1]):
            hastes[i].append(bola)
            bola += 1
            colocado = True
            break
      if not colocado:
         break

   return bola - 1

if __name__ == "__main__":
   reps = int(input())
   for i in range(reps):
      print(torre_de_hanoi_matrix(int(input())))