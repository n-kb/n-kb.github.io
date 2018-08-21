<template>
	<div class="container">
		<div class="columns is-centered">
			<div class="column is-narrow">
				<div class="content">
					<p>
						My name is <b>Nicolas Kayser-Bril</b> and I like to understand how things work. 
					</p>
					<p> To do so, I use data. I crunch, grind, chew and squeeze numbers to extract meaning and tell stories.</p>

					<p>That's called data-driven journalism and I'm proud to have been one of the first ones to practice it in Europe.</p>

					<p>I co-founded and managed <a href="http://jplusplus.org" target="_blank">Journalism++</a> from 2011 to 2017. Before that, I was head of datajournalism at <a target="_blank" href="http://owni.fr">Owni</a>.</p>

					<p>You can reach me at <a href="mailto:hi@nkb.fr">hi@nkb.fr</a>, follow me on Twitter <a target="_blank" href="http://twitter.com/nicolaskb">@nicolaskb</a> and on <a target="_blank" href="http://facebook.com/nicolas.kayser-bril">Facebook</a> or add me on <a target="_blank" href="http://de.linkedin.com/pub/nicolas-kayser-bril/8/1a6/750/">LinkedIn</a>. </p>
					<hr />
					<p class="has-text-centered">In the past {{years_active}} years, I</p>
					<div class="columns">
						<div class="column has-text-centered training">
							conducted <div class="big_number">{{ events_number["Training"] }}</div> <span class="has-text-weight-bold">training sessions</span>
						</div>
						<div class="column has-text-centered article">
							wrote <div class="big_number">{{ events_number["Article"] }}</div> <span class="has-text-weight-bold">articles</span>
						</div>
						<div class="column has-text-centered conference">
							spoke at <div class="big_number">{{ events_number["Conference"] }}</div> <span class="has-text-weight-bold">conferences</span>
						</div>
						<div class="column has-text-centered interview">
							gave <div class="big_number">{{ events_number["Interview"] }}</div> <span class="has-text-weight-bold">interviews</span>
						</div>
						<div class="column has-text-centered project">
							carried out <div class="big_number">{{ events_number["Project"] }}</div> <span class="has-text-weight-bold">projects</span>
						</div>
					</div>
					<div class="has-text-centered">
						<vizevents :nodes="nodes"></vizevents>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import vizevents from './vizEvents.vue'
	import * as d3 from 'd3'
	import moment from 'moment'

	export default {
		name: 'home',
		components: {vizevents},
		data () {
			return {
				all_events: [],
				events_number: {
					"Training": 0,
					"Conference": 0,
					"Article": 0,
					"Project": 0,
					"Interview": 0
				},
				nodes: []
			}
		},
		computed: {
			years_active () {
				return moment().year() - 2010;
			}
		},
		created () {
			var self = this
			d3.csv("src/assets/events.csv").then(function(data) {
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

.big_number
	font-size: 2em

</style>
