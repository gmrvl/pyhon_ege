
heap_1 = 8
heap_2 = int(input())


def plus_1(heap):
    return heap + 1


def umn_2(heap):
    return heap * 2


print('Петя:', plus_1(heap_1)+heap_2, umn_2(heap_1)+ heap_2, plus_1(heap_2)+ heap_1, umn_2(heap_2)+ heap_1)

print('Ваня:', plus_1(plus_1(heap_1))+heap_2, umn_2(plus_1(heap_1))+ heap_2, plus_1(heap_2)+ plus_1(heap_1), umn_2(heap_2)+ plus_1(heap_1), '|',
      plus_1(umn_2(heap_1))+heap_2, umn_2(umn_2(heap_1))+ heap_2, plus_1(heap_2)+ umn_2(heap_1), umn_2(heap_2)+ umn_2(heap_1),'|',
      plus_1(heap_1)+plus_1(heap_2), umn_2(heap_1)+ plus_1(heap_2), plus_1(plus_1(heap_2))+ heap_1, umn_2(plus_1(heap_2))+ heap_1,'|',
      plus_1(heap_1)+umn_2(heap_2), umn_2(heap_1)+ umn_2(heap_2), plus_1(umn_2(heap_2))+ heap_1, umn_2(umn_2(heap_2))+ heap_1, '|')

print('Петя:', plus_1(plus_1(heap_1))+heap_2,'|',
       umn_2(plus_1(heap_1))+ heap_2,'|',
       plus_1(heap_2)+ plus_1(heap_1),'|',
       umn_2(heap_2)+ plus_1(heap_1), '|',
      plus_1(umn_2(heap_1))+heap_2, '|',
      umn_2(umn_2(heap_1))+ heap_2,'|',
       plus_1(heap_2)+ umn_2(heap_1),'|',
       umn_2(heap_2)+ umn_2(heap_1),'|',
      plus_1(heap_1)+plus_1(heap_2),'|',
       umn_2(heap_1)+ plus_1(heap_2),'|',
       plus_1(plus_1(heap_2))+ heap_1,'|',
       umn_2(plus_1(heap_2))+ heap_1,'|',
      plus_1(heap_1)+umn_2(heap_2),'|',
       umn_2(heap_1)+ umn_2(heap_2),'|',
       plus_1(umn_2(heap_2))+ heap_1,'|',
       umn_2(umn_2(heap_2))+ heap_1, '|',
      )
