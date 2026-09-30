from pathlib import Path
import json

p = Path(r'C:\Users\willi\OneDrive\Desktop\04. Recoevo\Proyecto_Usme_Analisis\05_Presentacion_Final\RECOEVO_Carrusel_Investigacion.html')
s = p.read_text(encoding='utf-8')
marker = s.rindex('const slides=')
start = s.index('[', marker)
slides, size = json.JSONDecoder().raw_decode(s[start:])
deck_pos = s.index('document.getElementById(', start)
prefix = s[:start]

by_title = {x.get('title',''): x for x in slides}
for x in slides:
    if x.get('type') == 'cover':
        x['lead'] = 'Hallazgos integrados de entrevistas y recorrido de campo'
        x['sub'] = 'Voces del sector · recorrido del 20 de septiembre de 2026 · RECOEVO'
    if x.get('type') == 'map':
        x['title'] = 'Villarrosita, en Usme'
        x['lead'] = 'Un punto para ubicar el trabajo de campo en el suroriente de Bogotá.'
        x['sub'] = 'El pin es una referencia del enlace compartido. No define los límites del barrio ni la ruta completa.'
    if x.get('type') == 'photo' and 'punto de basura' in x.get('title','').lower():
        x['title'] = 'El chute y la basura que queda alrededor'
        x['lead'] = 'En la imagen se ve un aviso que prohíbe botar residuos y basura suelta dentro y alrededor del depósito. Varias entrevistas describen problemas parecidos de bolsas abiertas y residuos dispersos.'
        x['source'] = 'Foto de campo · 20 sep 2026 · la imagen no muestra quién dejó los residuos.'
    if x.get('type') == 'chart':
        x['title'] = 'Lo que más se repite en los turnos de participantes'
        x['lead'] = 'Las referencias a dejar y recoger la basura aparecen más veces que las referencias a separar residuos. Cada barra cuenta turnos etiquetados; no personas.'
        x['sub'] = '320 turnos de participantes · etiquetas exploratorias que pueden cruzarse.'
    if x.get('type') == 'quote' and 'separación' in x.get('title',''):
        x['title'] = 'En distintas entrevistas, los residuos van juntos en la bolsa'
        x['side'] = 'En otras voces también aparecen el afán, la distancia al punto y la duda sobre cuándo pasa el camión.'
    if x.get('type') == 'photoquote' and 'Las bolsas abiertas' in x.get('title',''):
        x['title'] = 'Las bolsas abiertas conectan el punto con la calle'
        x['lead'] = 'Distintas entrevistas cuentan que la basura queda en esquinas, se abre y se dispersa; las fotos muestran residuos dentro y fuera del depósito.'
    if x.get('type') == 'photo' and x.get('title','').startswith('Restos de cocina'):
        x['title'] = 'Restos de comida aparecen junto a otros residuos'
        x['lead'] = 'La foto muestra restos de alimentos, bolsas y envases en el mismo espacio. Varias entrevistas cuentan que la separación no suele ocurrir en origen.'
    if x.get('type') == 'photoquote' and ('animales' in x.get('title','').lower() or 'perros' in x.get('title','').lower()):
        x.pop('photo', None)
        x['video'] = 'clip_02.mp4'
        x['title'] = 'Perros y residuos comparten espacio'
        x['lead'] = 'La secuencia muestra perros cerca de bolsas y residuos. Varias voces dicen que buscan comida o rompen bolsas. El video no permite saber si están abandonados.'
        x['source'] = 'Video de campo · 7.47 a. m. · 13 s · audio silenciado'
    if x.get('type') == 'quote' and 'Comercios y hogares' in x.get('title',''):
        x['title'] = 'Hogares y comercios relatan prácticas distintas'
        x['lead'] = 'En el conjunto aparecen tanto restos mezclados como sobras que se ofrecen a los perros. Las entrevistas no describen una práctica igual para todos.'
    if x.get('type') == 'split':
        x['title'] = 'La recolección aparece de forma desigual en los relatos'
        x['lead'] = 'Varias entrevistas mencionan horarios inciertos, puntos que quedan lejos o sitios donde el camión no pasa. También se cuenta que algunas personas llevan las bolsas al punto disponible.'
    if x.get('type') == 'photo' and 'pavimento' in x.get('title',''):
        x['title'] = 'El recorrido muestra pavimento junto a suelo húmedo'
        x['lead'] = 'En esta toma, la vía pavimentada bordea un tramo de tierra húmeda y agua acumulada. Es una escena localizada, no una medida de todas las calles.'
    if x.get('type') == 'photoquote' and 'más de una esquina' in x.get('title',''):
        x['title'] = 'Las voces sitúan residuos en varias esquinas'
    if x.get('type') == 'contrast':
        x['title'] = 'Hay opiniones distintas sobre cuánto resuelve el chute'
        x['lead'] = 'Algunas voces dicen que sí ayuda; otras describen bolsas abiertas, basura en esquinas o fallas de recolección. Las dos caras aparecen en este mismo conjunto.'
    if x.get('type') == 'flow':
        x['title'] = 'Las voces conectan cuatro momentos del desorden'
        x['lead'] = 'Las entrevistas relacionan restos mezclados, bolsas dejadas fuera del punto o a destiempo, bolsas abiertas y residuos que se dispersan.'
        x['sub'] = 'Síntesis de relatos de distintas entrevistas; no todos los pasos se observaron en cada caso.'
    if x.get('type') == 'synthesis':
        x['title'] = 'Villarrosita: cuatro señales, un problema compartido'
        x['lead'] = 'Los residuos se mezclan · el punto no siempre los contiene · los perros buscan alimento · la frecuencia del servicio y el estado de la vía forman parte del escenario.'
        x['sub'] = 'Síntesis integrada de entrevistas y observación. Cada tema se respalda en varias voces o se marca como observación visual.'
    if x.get('type') == 'method':
        x['title'] = 'Ficha técnica · cómo leer estos resultados'
        x['lead'] = '10 audios emparejados con 10 transcripciones · 1:06:06 de grabación · 545 turnos extraídos · 22 fotos y 4 videos.'
        x['sub'] = '320 turnos de participantes para el conteo temático exploratorio. Las etiquetas pueden cruzarse. Audio2 dura 00:26 (fragmento breve) y Audio10 01:30 (permiso probable). Los tres OGG se midieron localmente. Personas únicas: pendientes de cotejo; nombres sólo cuando aparecen claramente. Video incluido en el hallazgo de perros: WhatsApp Video 2026-09-20 at 7.47.02 AM.mp4 (13 s). No se dibujan límites del barrio ni trayectos no georreferenciados.'
    if x.get('type') == 'thanks':
        x['title'] = 'Gracias'
        x['lead'] = 'RECOEVO · Barrio Villarrosita'
        x['sub'] = 'Lectura integrada de las voces y las escenas del recorrido.'

# Quotes must match a source turn exactly and remain anonymous under the reviewed consent form.
quote_sources = {
    'En distintas entrevistas, los residuos van juntos en la bolsa': ('“Pero como generalmente mantenemos esas las carreras, entonces uno que la cáscara de la papa a la misma bolsa, que el cartón, que esto, que las cáscaras de huevo, todo es un revoltijo.”','Entrevistado/a · Audio1-U018'),
    'Las bolsas abiertas conectan el punto con la calle': ('“...a esas bolsas que ya están hechas a desarmarlas y dejar un desorden por todo eso...”','Entrevistada · Audio8-U026'),
    'Perros y residuos comparten espacio': ('“...los animalitos de la calle, pues, también rebuscan ahí...”','Entrevistada · Audio8-U010'),
    'Hogares y comercios relatan prácticas distintas': ('“O sea, eso le echamos a los perritos cuando quieren comer.”','Entrevistada · Audio6-U019'),
    'La recolección aparece de forma desigual en los relatos': ('“Hace tres meses el carro no pasa por ahí.”','Entrevistada · Audio6-U037'),
    'Las voces sitúan residuos en varias esquinas': ('“En las esquinas, pero las esquinas mantienen llenas de basura.”','Entrevistada · Audio6-U034'),
}
for x in slides:
    if x.get('title') in quote_sources:
        x['quote'], x['by'] = quote_sources[x['title']]
    if x.get('type') == 'contrast':
        x['a'] = '“…sí es bueno ese chux, pero al mismo tiempo, pues no, porque no, no se beneficia uno en nada.”'
        x['b'] = '“Para nosotros no, porque nosotros cogemos la basura y la llevamos y la echamos a la comunidad.”'
        x['by'] = 'Entrevistado/a · Audio9-U020 / voz poco marcada · Audio7'
    if x.get('type') == 'method':
        x['sub'] = '320 turnos de participantes para el conteo temático exploratorio. Audio2 dura 00:26 y Audio10 01:30 (permiso probable). Personas únicas: pendientes de cotejo. La autorización revisada pide citas sin nombre: se identifican por audio y turno. Un video de 13 s se integra en el hallazgo de perros. El pin no marca límites del barrio ni trayectos georreferenciados.'

rest = s[deck_pos:]
old_img = r"""${s.photo?`<img class="photo" src="media/${esc(s.photo)}" alt="${esc(s.title)}">`:''}"""
new_img = r"""${s.video?`<video class="photo video-evidence" autoplay muted loop playsinline aria-label="${esc(s.title)}"><source src="media/${esc(s.video)}" type="video/mp4"></video>`:s.photo?`<img class="photo" src="media/${esc(s.photo)}" alt="${esc(s.title)}">`:''}"""
if old_img in rest:
    rest = rest.replace(old_img, new_img)
elif 's.video?`<video' not in rest:
    raise SystemExit('Image/video renderer not found')
old_obs = "const observer=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.querySelector('.progress i').style.width=((Array.from(deck.children).indexOf(e.target)+1)/slides.length*100)+'%'}),{root:deck,threshold:.6});"
new_obs = "const observer=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.querySelector('.progress i').style.width=((Array.from(deck.children).indexOf(e.target)+1)/slides.length*100)+'%';let v=e.target.querySelector('video');if(v)v.play().catch(()=>{});}else{let v=e.target.querySelector('video');if(v)v.pause();}}),{root:deck,threshold:.6});"
if old_obs in rest:
    rest = rest.replace(old_obs, new_obs)
if '.video-evidence{' not in prefix:
    prefix = prefix.replace('.cover,.thanks,.synth{grid-template-columns:1.1fr .9fr}', '.video-evidence{background:#132217}.cover,.thanks,.synth{grid-template-columns:1.1fr .9fr}')
s = prefix + json.dumps(slides, ensure_ascii=False) + ';const deck=' + rest
p.write_text(s, encoding='utf-8')
print(f'Reparada presentación: {len(slides)} láminas; {sum(bool(x.get("video")) for x in slides)} video integrado.')

