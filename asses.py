class Story:
    def __init__(self, age_group, length, moral_lesson):
        self.age_group = age_group
        self.length = length
        self.moral_lesson = moral_lesson

    def get_scope(self):
        return self.length

    def get_lesson(self):
        return self.moral_lesson

    def get_group(self):
        return self.age_group


class StoryTeller:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def get_details(self):
        return self.name


story = Story("12 to 15 years", 3, "Do not steal")
print(story.get_scope())

lesson = Story("5 to 10 years", 7, "Respecting Parents")
print(lesson.get_lesson())

group = Story("4 to 6 years", 1, "Praying everyday")
print(group.get_group())

teller = StoryTeller("Faith", 68, "Kikuyu")
print(teller.get_details())



class Recipe:
   def __init__(self, preparationTime, ingredients, cookingMethod, nutritionalInfo, country):
       self.preparationTime = preparationTime
       self.ingredients = ingredients
       self.cookingMethod = cookingMethod
       self.nutritionalInfo = nutritionalInfo
       self.country = country


   def recipes(self):
       print(f"{self.country}'s recipe, which takes {self.preparationTime} to be prepared by the {self.cookingMethod} method using {self.ingredients} as the ingredients, is very nutritive.")




class MoroccanRecipe(Recipe):
   def __init__(self, preparationTime, ingredients, cookingMethod, nutritionalInfo, country, spices):
       super().__init__(preparationTime, ingredients, cookingMethod, nutritionalInfo, country)
       self.spices = spices


   def describe(self):
       print(f"Eating Moroccan food that is {self.nutritionalInfo}, has {self.spices}.")




class EthiopianRecipe(Recipe):
   def __init__(self, preparationTime, ingredients, cookingMethod, nutritionalInfo, country, fatLevels):
       super().__init__(preparationTime, ingredients, cookingMethod, nutritionalInfo, country)
       self.fatLevels = fatLevels


   def describe(self):
       print(f"Anjera is a common meal prepared in {self.country} which is renowned for its {self.fatLevels}.")




class NigerianRecipe(Recipe):
   def __init__(self, preparationTime, ingredients, cookingMethod, nutritionalInfo, country, flavor, name):
       super().__init__(preparationTime, ingredients, cookingMethod, nutritionalInfo, country)
       self.flavor = flavor
       self.name = name


   def describe(self):
       print(f"{self.name} is the main dish in {self.country} whose {self.flavor} makes it unique.")




recipe = Recipe("3 hours", "Pepper", "boiling", "Provides vitamins", "Kenya")
recipe.recipes()


moroccan = MoroccanRecipe("2 hours", "Beef", "Deep frying", "Rich in proteins", "Morocco", "Ginger")
moroccan.describe()


ethiopian = EthiopianRecipe("2 days", "vegetables", "baking", "rich in proteins", "Ethiopia", "low fat levels")
ethiopian.describe()


nigerian = NigerianRecipe("1 hour", "rice and onions", "fried", "rich in carbohydrates", "Nigeria", "tomato flavor", "Jollof Rice")
nigerian.describe()


class Species:
    def __init__(self, name, diet, lifespan, month):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.month = month
    def track(self):
        if self.month<=0:
            return 'Month not available'
        elif self.month<=6:
            migration_pattern = 'South to East'
            return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Prey:{self.prey}\n Migration pattern:{migration_pattern}"
        elif self.month>=6 and self.month<=12:
            migration_pattern = 'North to West'
            return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Migration pattern:{migration_pattern}"
        return 'Month is in the  calendar'
class Predator(Species):
    def __init__(self, name, diet, lifespan, month, prey):
        super().__init__(name, diet, lifespan, month)
        self.prey = prey
    def track_predator(self):
        track = super().track()
        return f"{track}\n Prey:{self.prey}"
class Prey(Species):
    def __init__(self, name, diet, lifespan, month, predator):
        super().__init__(name, diet, lifespan, month)
        self.predator = predator
    def track_prey(self):
        track = super().track()
        return f"{track}\n Predator:{self.predator}"
animal_one = Predator('Lion', 'Herbivores', '30yrs', 13, ['Antelopes', 'Gazelles', 'Zebras'])
print(animal_one.track_predator())
animal_two = Prey('Zebra', 'Grass', '8yrs', 7, ['Cheetah', 'Lion', 'Black Panther'])
print(animal_two.track_prey())