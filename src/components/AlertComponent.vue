<template>
    <div v-if="success" class="alert alert-success alert-dismissible" role="alert">
        {{ message }}
    </div>
    <div v-else class="alert alert-danger alert-dismissible" role="alert">
        {{ message }}
    </div>
</template>

<script>
export default {
    props: ['message', 'success'],
    data() {
        return {};
    },
    mounted() {
        setTimeout(() => {
            this.$emit('hide');
        }, 5000);
    },
};
</script>

<style>
.alert {
    position: absolute !important;
    top: 10px !important;
    right: 10px !important;
    z-index: 100;
}
</style>
