import creature
import random
import copy
import math

def crossover_mutate(creatures, mutation_rate):
  #Calculate fitness scale for each creature to determine how likely they are to pass on their genes
  #Find mininum fitness
  min_fitness = math.inf
  for creature in creatures:
    min_fitness = min(min_fitness, creature.life)
  #Positive shift life to remove any negative life
  for creature in creatures:
    creature.positive_life = creature.life - min_fitness
  #Find total fitness of all creatures
  total_positive_life = sum(creature.positive_life for creature in creatures)
  if total_positive_life != 0: 
    for creature in creatures:
      #Find proportion of total life that creature held (i.e. their gene share)
      creature.scale = creature.positive_life / total_positive_life
  else: #Edge case: total_life = 0 would incur a divide by 0
    num_creatures = len(creatures)
    for creature in creatures:
      #All creatures must have attained 0 life so should be given equal gene shares
      creature.scale = 1 / num_creatures

  copy_creatures = copy.deepcopy(creatures) #Deep copy creatures
  sorted_parents = sorted(copy_creatures, key=lambda x: x.life) #Sort copied creatures to serve as parents
  new_creatures = sorted(creatures, key=lambda x: x.life)       #Sort original creatures to serve as new creatures

  for creature_index, new_creature in enumerate(new_creatures):
    for layer_index, layer in enumerate(new_creature.weights):
      for row_index, row in enumerate(layer):
        for gene_index, gene in enumerate(row):
          mutation_chooser = random.uniform(0, 1)
          if mutation_chooser < mutation_rate:
            new_creatures[creature_index].weights[layer_index][row_index][gene_index] = random.uniform(0, 1)
            break
          parent_chooser = random.uniform(0, 1)
          cumulated_probability = 0
          for possible_parent in sorted_parents:
            cumulated_probability += possible_parent.scale
            if cumulated_probability > parent_chooser:
              new_creatures[creature_index].weights[layer_index][row_index][gene_index] = possible_parent.weights[layer_index][row_index][gene_index]
              break
  return new_creatures
