import main
import media

toy_story=media.Movie("Toy Story","A story of a boy and his toys that come to life", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

#print toy_story.storyline

#toy_story.show_trailer()
tangled=media.Movie("Tangled","A story of a creative and beautiful girl with long hairs","https://lumiere-a.akamaihd.net/v1/images/open-uri20150608-27674-10u3zar_e7b16b8b.jpeg?region=0,0,1024,428","https://www.youtube.com/watch?v=pyOyBVXDJ9Q")

inside_out=media.Movie("Inside Out","A story of human mind and different emotions", "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE", "https://www.youtube.com/watch?v=seMwpP0yeu4")

panda=media.Movie("Kung Fu Panda", "A story of hidden Marshal Arts talent of a Panda","http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg","https://www.youtube.com/watch?v=PXi3Mv6KMzY")

frozen=media.Movie("Frozen", "A Story of two loving sisters and Elsa's Magic icy world","http://target.scene7.com/is/image/Target/57626-160613_1465794713056?wid=1200&fmt=pjpeg&qlt=80","https://www.youtube.com/watch?v=FLzfXQSPBOg")

nemo=media.Movie("Finding Nemo","A Story of a cute nemo fish and the father","http://www.welcomeamerica.com/wp-content/uploads/2016/04/nemo.jpg","https://www.youtube.com/watch?v=2zLkasScy7A")

puss=media.Movie("Puss in Boots","A Story of Puss","https://upload.wikimedia.org/wikipedia/en/1/1d/The_Adventures_of_Puss_in_Boots.jpg","https://www.youtube.com/watch?v=55gmAtakjJ4")

movies=[toy_story,tangled,inside_out,panda,frozen,nemo,puss]
main.open_movies_page(movies)

print (media.Movie.__doc__)
