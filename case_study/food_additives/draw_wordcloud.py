# Import the wordcloud library
from wordcloud import WordCloud # Join the different processed titles together.
from matplotlib import pyplot as plt

def draw_wordcloud(long_string, stpwrdlst, width = 2400, height = 2000, savefile = None):    

    font = r'C:\Windows\Fonts\simhei.ttf'
    
    wc = wordcloud = WordCloud(
        background_color="white", 
        max_words=5000, 
        contour_width=3, 
        font_path = font,
        width = width,
        height = height,
        stopwords = stpwrdlst,
        contour_color='steelblue')# Generate a word cloud
    wordcloud.generate(long_string)# Visualize the word cloud
    # wordcloud.to_image()
    
    plt.figure(figsize = (12,8))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

    if savefile:
        wc.to_file(savefile)