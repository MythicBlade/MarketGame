import matplotlib.pyplot as plt
from numpy import arange
from numpy import average
from matplotlib.colors import is_color_like



class Chart():
    def __init__(self,xdata,ydata,title = 'NewPlot', xlabel = 'xaxis',ylabel = 'yaxis',save = False,palette = 'muted_cool') -> None:
        
        
        #list of color palettes in format Name:[axis color, backround color, bar color]
        self.palettesList = {
            'muted_cool': ['#22223B', '#C9ADA7', '#4A4E69'],
            'muted_warm': ['#6D6875', '#FFCDB2', '#E5989B']} # TODO: CHECK THESE ONCE EVERYTHING IS WORKING MAKE SURE THEY ARE GOOD 
        
        if type(palette) is list:
            if len(palette) == 3:
                for c in palette:
                    if not(is_color_like(c)):
                        errorstring = f'{c} in your palette is not a valid color.'
                        raise ValueError(errorstring)
            else:
                errorstring  = f'Your Palette is {len[palette]} elements long it should be 3.'
                raise ValueError(errorstring)
        else:
            #choose color palette from list above
            try:
                self.palette = self.palettesList[palette]
            except KeyError as error:
                raise KeyError('''invalid color palette check the list of avalible palettes to see what
                                can be used or enter a list of 3 colors to define your own.''') from error

        
        #Set the Data
        self.xdata = xdata
        self.ydata = ydata

        #Set the label names
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        
        #Draw Initial Graph
        self.setupGraph()
        
    def drawGraph(self):
        # function to show the plot 
        plt.show() 

    def saveImage(self):
        #Save the Graph as a png
        self.fig.savefig(f'Data\\{self.title.replace(" ","")}.png')

    def setupGraph(self):
        # hide the toolbar and change axis color
        plt.rcParams['axes.edgecolor'] = self.palette[0]
        plt.rcParams['toolbar'] = 'None'
        #set the color
        self.fig = plt.figure(facecolor=self.palette[1])
        #make axes label and set colors
        ax = plt.axes()
        ax.set_facecolor(self.palette[1])
        ax.tick_params(colors=self.palette[0], which='both')
        # naming the axes
        plt.xlabel(self.xlabel,color = self.palette[0])
        plt.ylabel(self.ylabel,color = self.palette[0]) 
        # plot title 
        plt.title(f'{self.title}',color = self.palette[0]) 
        
    def makeLine(self): 
        #here we make the graph
        plt.plot(self.xdata, self.ydata, color = (self.palette[2])) \
        

    def makeBar(self):
        #here we make the graph
        plt.bar(self.xdata, self.ydata, tick_label = self.xdata, 
                width = 0.8,color = (self.palette[2])) 
    


x = Chart([1,2,3,4,5,6,7,8],[76,54,6,4,32,5,7,4])
x.makeLine()
x.drawGraph()