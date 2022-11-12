from transformers import pipeline

pipe = pipeline('text-generation', model='pranavpsv/genre-story-generator-v2')
text = pipe(" By forcing both Anakin and")
print(text)

'''
pipe = pipeline('text-generation', model='pjasminejwebb/KeywordIdentifier')
print(pipe('Anakin and Goro have a lot of trouble in their lives. Since the king is under duress from his father, his wife sends him away to the city (where they live happily). They have no one to turn to except Kizuma and Tsubasa, the wise-cracking, half-man half-sister of his father. To avoid conflict, both couples decide to marry and marry as little as possible, so the marriage of Kizuma with Goro begins.'))
'''
