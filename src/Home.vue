<template>
	<div class="container">
		<section class="hero is-fullheight">
			<div class="hero-body">
				<div class="content">
					<h1>
						<strong>Nicolas Kayser-Bril</strong> {{texts.is_professionally_curious[lang]}}.
					</h1>

				     <div class="has-text-centered">
			           <a class="tag" :class="{'is-hidden':lang=='en'}" @click="switchLang('en')">
			             Read in English
			           </a>
			           <a class="tag " :class="{'is-hidden':lang=='fr'}" @click="switchLang('fr')">
			             Lire en français
			           </a>
			           <a class="tag " :class="{'is-hidden':lang=='de'}" @click="switchLang('de')">
			             Auf Deutsch lesen
			           </a>
				     </div>

					<h2 v-html="texts.subtitle_1[lang]"></h2>
					<h2 v-html="texts.subtitle_2[lang]"></h2>
				</div>

			</div>
		</section>
		<section class="hero">
		  <div class="hero-body content">
		    <p class="title">
		      Nicolas Kayser-Bril <span class="books" v-html="texts.writes_books[lang]"></span>
		    </p>
		  </div>
		</section>
		<section class="section imposture book-spread">
			<div class="columns is-centered">
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782491241933-imposture-a-temps-complet-pourquoi-les-bullshit-jobs-envahissent-le-monde-nicolas-kayser-bril/"><img src="public/images/imposture-couve.jpg"></a>
				</div>
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782491241933-imposture-a-temps-complet-pourquoi-les-bullshit-jobs-envahissent-le-monde-nicolas-kayser-bril/"><img src="public/images/imposture-4e.png"></a>
				</div>
			</div>
		</section>
		<section class="section voracisme book-spread">
			<div class="columns is-centered">
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782490698264-voracisme-trois-siecles-de-suprematie-blanche-dans-l-assiette-nicolas-kayser-bril/"><img src="public/images/voracisme-couve.jpg"></a>
				</div>
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782490698264-voracisme-trois-siecles-de-suprematie-blanche-dans-l-assiette-nicolas-kayser-bril/"><img src="public/images/voracisme-4e.jpg"></a>
				</div>
			</div>
		</section>
		<section class="section breuvages book-spread">
			<div class="columns is-centered">
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782490698042-breuvages-bluffants-lait-biere-vin-the-cafe-la-veritable-histoire-de-nos-boissons-preferees-nicolas-kayser-bril/"><img src="public/images/breuvages-couve.jpg"></a>
				</div>
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782490698042-breuvages-bluffants-lait-biere-vin-the-cafe-la-veritable-histoire-de-nos-boissons-preferees-nicolas-kayser-bril/"><img src="public/images/breuvages-4e.png"></a>
				</div>
			</div>
		</section>
		<section class="section bouffes book-spread">
			<div class="columns is-centered">
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782955966051-bouffes-bluffantes-la-veritable-histoire-de-la-nourriture-de-la-prehistoire-au-kebab-nicolas-kayser-bril/"><img src="public/images/bouffes-couve.jpg"></a>
				</div>
				<div class="column has-text-centered">
					<a href="https://www.placedeslibraires.fr/livre/9782955966051-bouffes-bluffantes-la-veritable-histoire-de-la-nourriture-de-la-prehistoire-au-kebab-nicolas-kayser-bril/"><img src="public/images/bouffes-4e.jpg"></a>
				</div>
			</div>
		</section>
		<section class="hero">
		  <div class="hero-body content">
		    <p class="title">
		      Nicolas Kayser-Bril <span v-html="texts.phd[lang]" class="PhD" >studies for a PhD</span>
		    </p>
		  </div>
		</section>
		<section class="section is-size-4">
		  <div class="columns is-centered">
		  	<div class="column content" v-html="texts.phd_body[lang]">
			    
			 </div>
			 <div class="column has-text-centered">
			 	<img src="public/images/1910-V%C3%A9g%C3%A9taline.jpg">
			 </div>
		  </div>
		</section>
		<section class="hero">
		  <div class="hero-body content">
		    <p class="title">
		      Nicolas Kayser-Bril <span class="journalist" v-html="texts.journalist[lang]"></span>
		    </p>
		  </div>
		</section>
		<section class="section is-size-4">
		  <div class="columns is-centered">
		  	<div class="column content" v-html="texts.journalist_body[lang]">
			    
			 </div>
			 <div class="column content">
			 	<p v-html="texts.journalism_stories[lang]"></p>
			 	<ul class="is-size-5">
			 		<li><a href="https://www.mediapart.fr/journal/international/010221/comment-de-petits-escrocs-font-fermer-des-comptes-instagram?onglet=full">Comment de petits escrocs font fermer des comptes Instagram</a>, Mediapart, 2021.</li>
			 		<li><a href="https://algorithmwatch.org/en/instagram-algorithm-nudity/">Undress or fail: Instagram’s algorithm strong-arms users into showing skin</a>, AlgorithmWatch, 2020.</li>
			 		<li><a href="https://www.lemonde.fr/pixels/article/2019/07/26/sur-tinder-les-hommes-et-les-femmes-evoluent-dans-des-mondes-paralleles_5493933_4408996.html">Sur Tinder, les hommes et les femmes évoluent dans des mondes parallèles</a>, Le Monde, 2019.</li>
			 		<li><a href="https://www.spiegel.de/wissenschaft/natur/klimawandel-europaeische-staedte-erwaermen-sich-a-1228896.html">Wie sich unser Kontinent erwärmt</a>, Der Spiegel, 2018.</li>
			 		<li><a href="https://www.lexpress.fr/actualite/politique/fn-et-extreme-droite-des-partis-comme-les-autres-la-preuve-par-les-donnees_1870721.html">FN et extrême droite, des partis comme les autres: la preuve par les données </a>, L'Express, 2017.</li>
			 		<li><a href="https://www.theguardian.com/world/2014/jan/24/africa-clinton">Africa is not a country</a>, The Guardian, 2014.</li>
			 		<li><a href="https://www.huffingtonpost.fr/nicolas-kayserbril/cyberparc-corruption-algerie_b_3199235.html?just_reloaded=1">Algérie: Bienvenue au Cyberparc-Potemkine</a>, Huffington Post, 2013.</li>
			 	</ul>
			 </div>
		  </div>
		</section>
		<section class="hero">
		  <div class="hero-body content">
		    <p class="title">
		      Nicolas Kayser-Bril <span class="teaches" v-html="texts.teaches[lang]"></span>
		    </p>
		  </div>
		</section>
		<section class="section is-size-4">
		  <div class="columns is-centered">
		  	<div class="column content" v-html="texts.teaches_body[lang]">
			    
			 </div>
			 <div class="column content has-text-centered">
			 	<img src="/public/images/NicolasK.png">
			 	<p class="is-size-6" v-html="texts.teaches_legend[lang]"></p>
			 </div>
		  </div>
		</section>
		<section class="hero">
		  <div class="hero-body content">
		    <p class="title">
		      Nicolas Kayser-Bril <span class="blog" v-html="texts.blogs[lang]">blogs</span>
		    </p>
		  </div>
		</section>
		<section class="section">
			<div class="columns is-centered">
				<div class="column is-narrow">
					<div class="content">
						<div class="has-text-centered margin-top">
							<articleslist :articles="articles"></articleslist>
						</div>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script>
	import articleslist from './articlesList.vue'
	import { csv } from 'd3-fetch'
	import moment from 'moment'

	export default {
		name: 'home',
		components: {articleslist},
		data () {
			return {
				all_events: [],
				articles: [],
				blog_posts: 0,
				lang: "en",
				texts: {
					"is_professionally_curious": {
						"en": "is professionally curious",
						"fr": "est un curieux professionel",
						"de": "ist beruflich neugierig"
					},
					"subtitle_1": {
						"en": 'He writes <span class="books">books</span>, studies for a <span class="PhD">PhD</span>, works as a <span class="journalist">journalist</span>, <span class="teaches">teaches</span> and <span class="teaches">speaks</span>, and he <span class="blog">blogs</span>.',
						"fr": 'Il écrit <span class="books">des livres</span>, étudie pour un <span class="PhD">doctorat</span>, travaille en tant que <span class="journalist">journaliste</span>, <span class="teaches">enseigne</span> et donne des <span class="teaches">conférences</span>, et il <span class="blog">blogue</span>.',
						"de": 'Er schreibt <span class="books">Bücher</span>, studiert als <span class="PhD">Doktorand</span>, arbeitet als <span class="journalist">Journalist</span>, <span class="teaches">doziert</span> und <span class="teaches">trainiert</span>, und er <span class="blog">blogt</span>.'
					},
					"subtitle_2": {
						"en": 'You can follow him on <a target="_blank" href="http://twitter.com/nicolaskb">Twitter</a>, <a target="_blank" href="http://facebook.com/nicolas.kayser-bril">Facebook</a> or <a target="_blank" href="http://de.linkedin.com/pub/nicolas-kayser-bril/8/1a6/750/">LinkedIn</a>. Or send him an e-mail at hi@nkb.fr.',
						"fr": 'Vous pouvez le suivre sur <a target="_blank" href="http://twitter.com/nicolaskb">Twitter</a>, <a target="_blank" href="http://facebook.com/nicolas.kayser-bril">Facebook</a> ou <a target="_blank" href="http://de.linkedin.com/pub/nicolas-kayser-bril/8/1a6/750/">LinkedIn</a>. Ou lui envoyer un e-mail à hi@nkb.fr.',
						"de": 'Er ist auf <a target="_blank" href="http://twitter.com/nicolaskb">Twitter</a>, <a target="_blank" href="http://facebook.com/nicolas.kayser-bril">Facebook</a> oder <a target="_blank" href="http://de.linkedin.com/pub/nicolas-kayser-bril/8/1a6/750/">LinkedIn</a> zu folgen. Oder per Email unter hi@nkb.fr zu erreichen.'
					},
					"writes_books": {
						"en": "writes books",
						"fr": "écrit des livres",
						"de": "schreibt Bücher"
					},
					"phd": {
						"en": "studies for a PhD",
						"fr": "est doctorant",
						"de": "ist Doktorand"
					},
					"phd_body": {
						"en":'<p>I began a PhD under the supervision of Prof. Günther Hirschfelder at the University of Regensburg.</p><p>I research the cultural history of edible vegetable oils in France and Germany between 1871 and 1933. It has to do with food, race and business economics. </p><p>I wrote a summary of the project here: <a href="https://blog.nkb.fr/fats/">The colonial roots of French fries</a>.</p>',
						"fr":'<p>J\'ai commencé un doctorat sous la direction du prof. Günther Hirschfelder à l\'université de Ratisbonne.</p><p>Je m\'intéresse à l\'histoire culturelle des matières grasses alimentaires en France et en Allemagne entre 1871 et 1933. C\'est une histoire de race, d\'empire, d\'alimentation et d\'économie. </p><p>J\'ai écrit ici un résumé du projet&nbsp;: <a href="https://blog.nkb.fr/fats/">The colonial roots of French fries</a>.</p>',
						"de":'<p>Ich habe eine Doktorarbeit unter Betreuung von Prof. Günther Hirschfelder an der Universität Regensburg angefangen.</p><p>Ich recherchiere kolonialische pflanzliche Öle in Frankreich und Deutschland zwischen 1871 und 1933. Es geht um Rasse, Essen und Wirtschaft. </p><p>Ich habe eine Zusammenfassung des Projekts hier geschrieben: <a href="https://blog.nkb.fr/fats/">The colonial roots of French fries</a>.</p>'
					},
					"journalist": {
						"en": "works as a journalist",
						"fr": "est journaliste",
						"de": "arbeitet als Journalist"
					},
					"journalist_body": {
						"en": '<p>I work as a journalist for <a href="https://algorithmwatch.org/">AlgorithmWatch</a>.</p><p>I pioneered data-driven journalism in Europe since circa 2006, at <a href="http://owni.fr/">OWNI.fr</a> and then at Journalism++, which I co-founded.</p><p>🏆 I was awarded the Excellence in Journalism for non-English websites (small) award by the Online News Association in 2010 with <a href="http://owni.fr/">OWNI</a>, the Datajournalism Award (Best story) in 2014 and the European Press Prize (category innovation) in 2015 for <a href="https://www.themigrantsfiles.com/">The Migrants\' Files</a>.</p>',
						"fr": '<p>Je suis journaliste pour <a href="https://algorithmwatch.org/">AlgorithmWatch</a>.</p><p>Commençant vers 2006, j\'ai exploré le datajournalisme à <a href="http://owni.fr/">OWNI.fr</a> d\'abord, puis au sein de Journalism++, que j\'ai cofondé.</p><p>🏆 J\'ai reçu le prix de l\'Excellence in Journalism for non-English websites (small) de la Online News Association en 2010 avec <a href="http://owni.fr/">OWNI</a>, le Datajournalism Award (Best story) en 2014 et le European Press Prize (catégorie innovation) en 2015 pour <a href="https://www.themigrantsfiles.com/">The Migrants\' Files</a>.</p>',
						"de": '<p>Ich bin Journalist bei <a href="https://algorithmwatch.org/">AlgorithmWatch</a>.</p><p>Ich habe den Weg für Datenjournalismus in Europa ab 2006 bereitet, zuerst bei <a href="http://owni.fr/">OWNI.fr</a>, dann bei Journalism++, die ich mitbegründet habe.</p><p>🏆 Meine Arbeit wurde mit dem Excellence in Journalism for non-English websites (small) Preis von der Online News Association 2010 mit <a href="http://owni.fr/">OWNI</a> ausgezeichnet, sowie mit dem Datajournalism Award (Best story) 2014 und dem European Press Prize (Kategorie Innovation) 2015 für <a href="https://www.themigrantsfiles.com/">The Migrants\' Files</a>.</p>'
					},
					"journalism_stories": {
						"en" : "Here are some stories I'm proud of:",
						"fr" : "Quelques articles dont je suis fier&nbsp;:",
						"de" : "Einige Artikel, die ich besonders mag:"
					},
					"teaches" : {
						"en": "teaches and speaks",
						"fr": "enseigne et donne des conférences",
						"de": "doziert und trainiert"
					},
					"teaches_body": {
						"en": '<p>  I love provoking new ways of thinking among students and professionals. I conducted over 100 training sessions since 2007, on all continents except Oceania and Antartica.</p><p>I taught datajournalism at ESJ (Lille), CFJ (Paris), HSE (Moscow), HMKW (Berlin), AJM (Neuchâtel) and many more.			    </p><p>I gave keynotes at Société Générale, Tamedia, Le Figaro, Sanoma, Prisma and others.</p>',
						"de": '<p>Ich mag es besonders gern, neue Denkweisen bei Student:innen oder Erwerbstätigen zu erregen. Seit 2007 habe ich mehr als 100 Trainings aller Art über alle Kontinente außer Ozeanien und der Antarktis geführt.</p><p>Ich habe Datenjournalismus an den ESJ (Lille), CFJ (Paris), HSE (Moskau), HMKW (Berlin), AJM (Neuenburg) und viel andere gelehrt.			    </p><p>Ich war Redner in privaten Konferenzen bei Société Générale, Tamedia, Le Figaro, Sanoma, Prisma und mehr.</p>',
						"fr": '<p>J\'aime beaucoup partager des idées nouvelles avec des étudiant·es ou des professionel·les. Depuis 2007, j\'ai animé plus d\'une centaine de formations en tous genres, sur tous les continents sauf l\'Océanie et l\'Antarctique.</p><p>J\'ai enseigné le datajournalisme à l\'ESJ (Lille), au CFJ (Paris), la HSE (Moscow), la HMKW (Berlin), l\'AJM (Neuchâtel) et beaucoup d\'autres.			    </p><p>J\'ai également animé des conférences privées à la Société Générale, Tamedia, Le Figaro, Sanoma ou Prisma, entre autres.</p>'
					},
					"teaches_legend": {
						'en': 'At OuestMediaLab (Nantes) in 2018.',
						'fr': 'À OuestMediaLab (Nantes) en 2018.',
						'de': 'Bei OuestMediaLab (Nantes) 2018.'
					},
					"blogs": {
						'en': 'blogs',
						'de': 'blogt',
						'fr': 'blogue'
					}
				}
			}
		},
		methods: {
			switchLang(lang) {
				this.lang = lang
			}
		},
		created () {

			var lang = navigator.language.substring(0,2)
			if (["fr", "de"].indexOf(lang)) { this.switchLang(lang) }

			var self = this
			csv('./public/assets/articles.csv').then(function(data) {
				data.forEach(function(article){
					var article_date = moment(article.date, "MMMM D, YYYY");
					self.articles.push({
						"title": article.title,
						"lang": article.lang,
						"is_external": article.is_external,
						"url": article.url,
						"date": article_date.format("MMMM Do, YYYY"),
					})
					self.blog_posts++
				});
			});
		}
		
	}
</script>

<style lang="sass">

@import "colors.sass"

.content
	font-family: Georgia, serif
	color: #4a4a4a

.content h1
	font-size: 2.5em;

.content h2
	font-size: 1.5em;

.input-nl
	font-family: Georgia, serif
	color: #4a4a4a

.PhD
	background-image: linear-gradient(transparent calc(95% - 3px), $nkb-red 3px);

.books
	background-image: linear-gradient(transparent calc(95% - 3px), $nkb-yellow 3px);

.teaches
	background-image: linear-gradient(transparent calc(95% - 3px), $nkb-lightblue 3px);

.journalist
	background-image: linear-gradient(transparent calc(95% - 3px), $nkb-darkblue 3px);

.blog
	background-image: linear-gradient(transparent calc(95% - 3px), $nkb-purple 3px);

.book-spread img
	max-height: 80vh;

.imposture
	background-color: #fbfac2;

.voracisme
	background-color: #d82e15;

.breuvages
	background-color: #02984e;

.bouffes
	background-color: #fdee00;

.project
	color: $nkb-lightblue
.interview
	color: $nkb-yellow
.article
	color: $nkb-red
.conference
	color: $nkb-darkblue
.training
	color: $nkb-purple

.margin-top
	margin-top: 2em

</style>
