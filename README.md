# Oxford Hackathon Nov 2022 - AutoMangaAnime
The following project is about generating manga and anime where the only input is two main characters and the rest is magic.

### Harry Potter and Darth Vader Manga ...
![Alt text](https://github.com/saradrag/oxhack/blob/main/manga.png)

### Harry Potter and Darth Vader Anime ...
##### Enable sound for the story telling
<video src="https://user-images.githubusercontent.com/112171137/201532458-dd5e9f3e-7323-4215-a55d-1cd546c3d9e6.mp4" controls="controls" style="max-width: 50%;">
</video>

### Shrek and Sponge Bob Anime ...
##### Enable sound for the story telling
<video src="https://user-images.githubusercontent.com/112171137/201532681-3831bdb8-0d85-4ad7-9afe-a4b368fc083c.mp4" controls="controls" style="max-width: 50%;">
</video>

### How to use

To use manga generating notebook: 

1. Open the Manga.ipnyb file in Colab (will need to download large models and do lots of computation, probably not a good idea to run on local machine).

2. Upload the .ttf font file to file - content - sample_data.

3. Change the `main_character` and `second_character` variables to anything you like. 

4. Run through the .ipnyb file step by step. It might take some time to download the models the first time you run it. 

5. Then a PNG file `manga.png` will be generated in Colab: file - content - sample_data. Have a look!

To use anime generating notebook:

1. Open the Anime.ipnyb file in Colab (will need to download large models and do lots of computation, probably not a good idea to run on local machine).

2. Change the text = pipe("Harry Potter and Darth Vader have") to whatever you like. 

3. Run through the .ipnyb file step by step. It might take some time to download the models the first time you run it. 

4. Then a video `my_video.mp4` will be generated in Colab: file - content. Have a look!

### Future

1. Bug: `NameError: name 'init_empty_weights' is not defined` appears sometimes. Try to restart the Colab session and hope it works.
