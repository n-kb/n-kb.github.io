<template>
	<div>
		<section class="hero">
		  <div class="hero-body">
		    <div class="container">
		      <div class="columns is-mobile">
		      	<div class="column content has-text-right">
		      		<h1>
		      			nkb
		      		</h1>
		      	</div>
		      	<div class="column has-text-left">
		      		<ul>
		      			<li class="interview is-uppercase has-text-weight-bold is-size-7">Journalist</li>
		      			<li class="article is-uppercase has-text-weight-bold is-size-7">Author</li>
		      			<li class="training is-uppercase has-text-weight-bold is-size-7">Trainer</li>
		      			<li class="conference is-uppercase has-text-weight-bold is-size-7">Public speaker</li>
		      			<li class="project is-uppercase has-text-weight-bold is-size-7">Project manager</li>
		      		</ul>
		      	</div>
		      </div>
		    </div>
		  </div>
		</section>
		<section class="section">
			<div class="columns is-centered">
				<div class="column is-narrow">
					<div class="content">
						<p>
							My name is <b>Nicolas Kayser-Bril</b> and I like to understand how things work. 
						</p>
						<p>
							I look at their histories and gather data. Some people say it's datajournalism, but I say it's just rigorous curiosity.
						</p>

						<p>
							I write <a href="https://www.placedeslibraires.fr/listeliv.php?base=paper&mots_recherche=Nicolas%20KAYSER-BRIL">books</a>, mostly about the history of food, and work as a reporter for <a href="http://algorithmwatch.org/">AlgorithmWatch</a>.
						</p>

						<p>I co-founded and managed <a href="http://jplusplus.org" target="_blank">Journalism++</a> from 2011 to 2017. Before that, I was head of datajournalism at <a target="_blank" href="http://owni.fr">Owni</a>.</p>

						<p>You can reach me at <a href="mailto:hi@nkb.fr">hi@nkb.fr</a>, follow me on Twitter <a target="_blank" href="http://twitter.com/nicolaskb">@nicolaskb</a> and on <a target="_blank" href="http://facebook.com/nicolas.kayser-bril">Facebook</a> or add me on <a target="_blank" href="http://de.linkedin.com/pub/nicolas-kayser-bril/8/1a6/750/">LinkedIn</a>. </p>

						<hr />
						
						<p class="has-text-centered">In the past {{years_active}} years, I</p>
						<div class="columns">
							<div class="column has-text-centered training">
								conducted <div class="is-size-3">{{ events_number["Training"] }}</div> <span class="has-text-weight-bold">training sessions</span>
							</div>
							<div class="column has-text-centered article">
								wrote <div class="is-size-3">{{ events_number["Article"] }}</div> <span class="has-text-weight-bold">articles</span>
							</div>
							<div class="column has-text-centered conference">
								spoke at <div class="is-size-3">{{ events_number["Conference"] }}</div> <span class="has-text-weight-bold">conferences</span>
							</div>
							<div class="column has-text-centered interview">
								gave <div class="is-size-3">{{ events_number["Interview"] }}</div> <span class="has-text-weight-bold">interviews</span>
							</div>
							<div class="column has-text-centered project">
								carried out <div class="is-size-3">{{ events_number["Project"] }}</div> <span class="has-text-weight-bold">projects</span>
							</div>
						</div>
						<div class="has-text-centered">
							<vizevents :nodes="nodes"></vizevents>
						</div>

						<hr/>
						<div class="has-text-centered">and, since I started my blog {{years_ago}} years ago, I published</div>
						<div class="is-size-3 has-text-centered">{{blog_posts}}</div>
						<div class="has-text-centered">blog entries, essays, short stories and even a poem!</div>
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
	import vizevents from './vizEvents.vue'
	import articleslist from './articlesList.vue'
	import { csv } from 'd3-fetch'
	import moment from 'moment'

	export default {
		name: 'home',
		components: {vizevents, articleslist},
		data () {
			return {
				all_events: [],
				articles: [],
				events_number: {
					"Training": 0,
					"Conference": 0,
					"Article": 0,
					"Project": 0,
					"Interview": 0
				},
				blog_posts: 0,
				nodes: []
			}
		},
		computed: {
			years_active () {
				return moment().year() - 2010;
			},
			years_ago () {
				return moment().year() - 2015;
			}
		},
		created () {
			var self = this
			csv('./public/assets/events.csv').then(function(data) {
		      	data.forEach(function(event){
			        var event_date = moment(event.startdate);
			        // Creates the object needed for the visualization
			        self.all_events.push({
			          "title": event.title,
			          "type": event.type,
			          "url": event.url,
			          "lat": event.lat,
			          "lon": event.lon,
			          "location": event.location,
			          "date": event_date,
			          "year": event_date.year(),
			          "day_of_year": event_date.dayOfYear()
			    	})
			    	// Increments the number of event of that type
			    	self.events_number[event.type]++
		      	});
			});
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
		},
		watch: {
			all_events: function() {
				this.nodes = this.all_events
			}
		}
		
	}
</script>

<style lang="sass">

@import "colors.sass"

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
