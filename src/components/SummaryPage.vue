<template>
    <div class="container">
        <img v-if='fetched' :src='images.booking' alt="">
        <img v-if='fetched' :src='images.rating' alt="">
    </div>
</template>

<script>
export default {
    data: () => {
        return {
            // venueId: this.$route.params.venueId,
            fetched : false,
            images : {
                booking : "",
                rating : ''
            }
        }
    },
    methods: {
        async getSummary(){
            try {
                await fetch(`http://127.0.0.1:8081/api/summary/${this.$route.params.venueId}`,
                    {
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });
                this.images.booking = require(`../assets/booking${this.$route.params.venueId}.png`)
                this.images.rating = require(`../assets/rating${this.$route.params.venueId}.png`)
                this.fetched = true
            } catch (error) {
                console.error('Error fetching summary stats:', error);
            }
        
        }
    },
    mounted() {
        this.getSummary()
    }
}
</script>

<style>
.container {
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    max-width: 100%;
    display: grid;
    grid-template-columns: 50% 50%;
}
.container>img {
    width: 110%;
}
</style>