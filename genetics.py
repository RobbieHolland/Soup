import creature
import random

def handle_end_episode(creatures, mutation_rate):
  copy_sorted_creatures = sorted(creatures, key=lambda x: x.life, reverse=True)
  total_fitness = sum(creature.life for creature in creatures)
  for creature in creatures:
    total_fitness += creature.life
  for creature in copy_sorted_creatures:
    creature_index += 1
    for layer in creature.weights:
      layer_index += 1
      for row in layer:
        row_index += 1
        for gene in row:
          gene_index += 1
          mutation_chooser = random.uniform(0, 1)
          if mutation_chooser < mutation_rate:
            gene = random.uniform(0, 1)
            break
          parent_chooser = random.uniform(0, 1)
          cumulated_probability = 0
          for possible_parent in copy_sorted_creatures:
            if cumulated_probability + possible_parent.life / total_fitness > parent_chooser:
              gene = possible_parent.weights[layer_index][row_index][gene_index]
  return copy_sorted_creatures      
