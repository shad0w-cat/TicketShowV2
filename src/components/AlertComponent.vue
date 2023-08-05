<template>
    <div v-if="success" class="alert alert-success" role="alert">
        This is a success alert—check it out!
    </div>
    <div v-else class="alert alert-danger" role="alert">
        {{ message }}
    </div>
</template>

<script>
export default {
    props: ['message', 'success'],
    data() {
        return {
        }
    }
}
</script>