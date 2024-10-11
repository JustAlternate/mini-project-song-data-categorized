# Etape 1

## Morceaux

(Règle imposée a moi même : Pas de répétition d'artiste)

1. The Killers - Mr. Brightside
2. Sum 41 - In Too Deep
3. Ultra Vomit - ÉVIER METAL
4. Porter Robinson - Goodbye To A World
5. My Chemical Romance - Welcome To The Black Parade
6. Smash Mouth - All Star
7. Green Day - Boulevard Of Broken Dreams
8. Marillion - Kayleigh
9. S3RL - Techno Kitty
8. John Williams - Imperial March
9. Hans Zimmer - Cornfield Chase
10. blink-182 - I Miss You
11. Queen – Bohemian Rhapsody
12. C418 - Sweden
13. Coldplay - Viva La Vida
14. Lena Raine - otherside
15. The OneUps - Kirby's Dream Land - Green Greens
16. Tomohito Nishiura - Professor Layton's Theme
17. Miki Matsubara - Stay With Me
18. Mariya Takeuchi - Plastic Love
19. Yumi Arai - Hikouki Gumo
20. Dragon Force - Through The Fire And Flames
21. succducc - me & u
22. Kuba Oms - My Love
23. Mrs. GREEN APPLE - インフェルノ(Inferno)
24. Xi - Freedom Dive
25. KANA-BOON - Silhouette
26. Neck Deep - December
27. Mayday Parade - Black Cat
28. Elton John - Rocket Man
29. The Wonder Years - Cardinals
30. Crystal Dolphin - Engelwood
31. Imagine Dragons - Warriors
32. Sleeping With Sirens - If You Can't Hang
33. Pierce The Veil - King for a Day
34. Noma - Brain Power
35. MAN WITH A MISSION - Raise your flag
36. Silent Siren - Routine
37. Bill Withers - Just The Two Of Us
38. VINXIS - Sidetracked Day
39. Reol - Asymmetry
40. Cartoon - Whatever I Do
41. YUC'e - Future Candy
42. Initial D - Deja Vu
43. Muse - Supermassive Black Hole
44. Ludwig Göransson - Can You Hear The Music
45. Hatsune Miku - Mythologia's End
46. BABYMETAL - Gimme chocolate!!
47. Nanaki - Mousou Kajitsu
48. Camellia - Exit this Earth's Atomosphere
49. Gloria Gaynor - Can't take my eyes off you
50. Pokémon - Champion Cynthia Battle Music

## Catégories

(Les Catégories ont étaient choisis avant d'avoir trouvé les morceaux)

1. Female vocal     (voix feminine majoritaire)
2. Male vocal       (voix masculine majoritaire)
3. Fast paced       (Rythme rapide ou très rapide)
4. Medium Slow      (Rythme lent ou moyen)
5. Strongly Emotive (Qui suscite fortement l'émotion)
6. English          (Majorité de paroles en Anglais)

Toutes les catégories seront assignées aux morceaux choisis sur la base du "feeling"
Ce qui signifie que si un morceau me semble "Emotif" alors, je le classerai dans la catégorie "Strongly Emotive".

Ainsi, les catégories 3,4 et 5 sont très biaisées par ma propre interprétation, car il n'existe pas de ce que j'appelle "*règle d'assignation binaire évidente*" pour ces catégories.

Le classement des morceau se trouve dans le fichier [data.yaml](./data.yaml)

### C'est quoi une "règle d'assignation binaire" ?

J'appelle une règle d'assignation binaire, une règle qui permet de répondre par oui ou non à la question "Est-ce que ce morceau appartient à cette catégorie ?"

Exemple :
On aurait pu imaginer que la catégorie "Fast paced" soit assignée suivant la règle d'assignation binaire : "Si le morceau a un BPM supérieur à 150, alors il est Fast Paced"

Grâce à cette règle, on peut savoir pour n'importe quel morceau de musique existant s'il appartient ou non à la catégorie "Fast Paced"

Par contre, on remarquera qu'il n'est pas toujours aussi facile de trouver une règle d'assignation binaire qui soit juste :

Par exemple, pour la catégorie "Strongly Emotive" il est assez difficile d'en trouver une qui a du sens :

On pourrait quand même inventer la règle suivante : "Si le morceau contient plus de 20 mots parmi le vocabulaire proche de l'émotion, alors il est Strongly Emotive".

Mais alors:

- Quid des morceaux sans paroles ?
- Quid de ce qu'est le "vocabulaire proche de l'émotion"
- ...

On pourra aussi constater que certaines catégories semblent dans certains cas avoir une règle d'assignation binaire *evidente* (plus simple a trouver):

Par exemple :

Pour la catégorie English: "Si un morceau a une majorité de paroles dans la langue Anglaise, alors il est English."

Pour ma conception de la catégorie English, cette règle semble parfaite, donc c'est pour moi *règle d'assignation binaire évidente*.

La question est donc la suivante : "Comment associer le plus justement possible des règles d'assignation a des catégories ?"

Imaginons une liste de catégories :

1. Rock
2. Heavy Metal
3. Punk Rock
4. Power Metal

Et une liste de règle :

1. "Has an electrical guitar"
2. "Has a drum"
3. "Has a bass"
4. "Has fantasy based lyrics"
5. "Has heavy bass"
6. "Has heavy drums"
7. "Has loud and distorded guitars"
8. "Has a fast tempo"
9. "Has sense a of Authenticity"


Une attribution correct pourrait être :

Rock : {1,2,3}
Heavy Metal : {1,2,3,5,6,7}
Punk Rock : {1,2,3,8,9}
Power Metal: {1,2,3,4,5,6,8}


