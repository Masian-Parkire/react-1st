class Story {
    constructor(ageGroup, length, moralLesson) {
      this.ageGroup = ageGroup;
      this.length = length;
      this.moralLesson = moralLesson;
    }
  
    getScope() {
      return this.length;
    }
  
    getLesson() {
      return this.moralLesson;
    }
  
    getGroup() {
      return this.ageGroup;
    }
  }
  
  class StoryTeller {
    constructor(name, age, language) {
      this.name = name;
      this.age = age;
      this.language = language;
    }
  
    getDetails() {
      return this.name;
    }
  }
  
  const story = new Story("12 to 15 years", 3, "Do not steal");
  console.log(story.getScope());
  
  const lesson = new Story("5 to 10 years", 7, "Respecting Parents");
  console.log(lesson.getLesson());
  
  const group = new Story("4 to 6 years", 1, "Praying everyday");
  console.log(group.getGroup());
  
  const teller = new StoryTeller("Faith", 68, "Kikuyu");
  console.log(teller.getDetails());
  

  class Species {
    constructor(name, diet) {
      this.name = name;
      this.diet = diet;
    }
     eat(food) {
      console.log(`${this.name} is eating ${food}.`);
    }
  }
  
  class Predator extends Species {
    constructor(name, diet, huntingStyle) {
      super(name, diet);
      this.huntingStyle = huntingStyle;
    }
     hunt(prey) {
      console.log(`${this.name} is hunting ${prey.name}.`);
       if (this.diet === prey.diet) {
        console.log(`Oops! ${this.name} and ${prey.name} have the same diet. ${this.name} cannot hunt ${prey.name}.`);
      } else {
        prey.getHunted(this);
      }
    }
  }
  
  class Prey extends Species {
    constructor(name, diet, migrationPattern) {
      super(name, diet);
      this.migrationPattern = migrationPattern;
    }
     migrate() {
      console.log(`${this.name} is migrating.`);
    }
     getHunted(predator) {
      console.log(`${this.name} is being hunted by ${predator.name}.`);
       if (predator.huntingStyle === "Stalking") {
        console.log(`${this.name} is alert and trying to evade ${predator.name}.`);
      } else {
        console.log(`${this.name} is running away from ${predator.name} as fast as possible.`);
      }
    }
  }
  
  const lion = new Predator("Lion", "Carnivorous", "Stalking");
  const zebra = new Prey("Zebra", "Herbivorous", "Seasonal");
  const gazelle = new Prey("Gazelle", "Herbivorous", "Yearly");
   lion.eat("Gazelle");
  lion.hunt(zebra);
  lion.hunt(gazelle);
  zebra.migrate()