# Name: Akshat Gaur
# Student ID: 2176685
# Date :11/10/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Links:
# Plot Generator: https://youtu.be/VKKovyjl7W0
# Plot Viewer: https://youtu.be/1Pm0krVjq2E

import random 

class SimplePlotGenerator:
    """
    Generates simple generic plot
    """
    fileList = ["plot_names.txt", "plot_adjectives.txt", "plot_profesions.txt", "plot_verbs.txt", "plot_adjectives_evil.txt", "plot_villian_job.txt", "plot_villains.txt"]

    def registerPlotViewer(self, pv):
        """
        Register a PlotViewer instance to the generator. (pv = Instance of plot viewer class)
        """
        self.pv = pv

    def generate(self):                         
        return "Something happens"                             # Returns generic plot

class RandomPlotGenerator(SimplePlotGenerator):
     """
     Inherits SimplePlotGenerator
     Generates random plot using various files
     """
     def generate(self):
         """
         Takes random words from each file mentioned.
         Returns a combined generated plot.
         """
         self.plotList=[]                                       
         for filename in self.fileList:                         # Going through all the files in the list
             wordList=[] 
             file = open(filename, "r")
             for word in file:
                 word = word.strip()                            # Removing whitespaces
                 wordList.append(word)                          # Appending all words in a list
             ranWord = random.choice(wordList)                  # Selecting a random word in the list of words
             self.plotList.append(ranWord)                      # Adding random words found to the plotList
             file.close()
             
         self.plot = "\n{}, a {} {}, must {} the {} {}, {}.".format(self.plotList[0],self.plotList[1],self.plotList[2],self.plotList[3],self.plotList[4],self.plotList[5],self.plotList[6])         # Combining the words of plotList to create a plot 

         return self.plot
        

class InteractivePlotGenerator(SimplePlotGenerator):
    """
    Inherits SimplePlotGenerator
    Generates random plot on the basis of interation with the user
    """
    def generate(self):
        """
        Takes 5 random words from each file mentioned.
        Passes on a query for a user to select one word out of 5
        Returns a combined generated plot.
        """
        self.plotList = []
        print("Select the number to generate plot")
        for filename in self.fileList:
            wordList = []
            file = open(filename, "r")
            for word in file:
                word = word.strip()                            # Removing whitespaces
                wordList.append(word)                          # Appending all words in a list
            ran_words = random.sample(wordList, 5)             # Selecting a random words sample(5 words) in the list of words

            choices = []
            for i, word in enumerate(ran_words, 1):            # Runs a loop through ran_words, creates index for them(starting with 1).
                choices.append(f"{i}. {word}")                 # Append each word from 'ran_words' to 'choices' with a human-friendly index
            print("\n")
            # Query user to select a word by displaying the available choices.
            result = self.pv.queryUser("\n".join(choices)+"\nPlease select one: ") 
            file.close()

            try:
                ask_word_index = int(result)                        # Converts the user's choice to integer
                self.plotList.append(ran_words[ask_word_index - 1]) # Appends the plotList according to the word user chooses
            except ValueError:                                      # In case the user has entered an invalid string
                print("Invalid input. Please enter a number.")

        self.plot = "{}, a {} {}, must {} the {} {}, {}.".format(self.plotList[0], self.plotList[1], self.plotList[2], self.plotList[3], self.plotList[4], self.plotList[5], self.plotList[6])
        return self.plot
    
class PlotViewer:
    """
    Used to display plots which are generated.
    """
    def registerPlotGenerator(self, pg):
        """
        Register a PlotGenerator instance to this viewer.
        """
        self.pg = pg                                  # Assigns 'pg' to the 'self.pg' attribute of the PlotViewer.
        self.pg.registerPlotViewer(self)              # Register the current PlotViewer instance with the assigned plot generator 'self.pg'.
    
    def queryUser(self, str):
        """
        Gets user input to generate interactive plots
        """
        return input(str)                             # Returns user input as string

    def generate(self):
        """
        Generate and display the plots generated
        """
        print (self.pg.generate())                    # Generate a plot using the registered plot generator and print it


pv = PlotViewer()                                     # Creating a plot viewer instance

print ("\nAttempting: Simple Generator")
pv.registerPlotGenerator(SimplePlotGenerator())       # Registering Simple plot generator with pv
pv.generate()

print ("\nAttempting: Random Generator")
pv.registerPlotGenerator(RandomPlotGenerator())       # Registering Random plot generator with pv
pv.generate()

print ("\nAttempting: Interactive Generator")
pv.registerPlotGenerator(InteractivePlotGenerator())  # Registering Interactive plot generator with pv
pv.generate()
