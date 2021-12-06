<template>
  <div>
    <!-- <button @click="increment">+</button> -->
    <button @click="incrementAction">+</button>
    <button @click="addCount">+10</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods:{
    // increment(){
    //   this.$store.commit('increment')
    // },
    // addCount(){
    //   this.$store.commit('addCount', { 
    //     value: 10
    //    })
    // }
    ...mapActions(['incrementAction', 'addCountAction']),
    // increment(){
    //   this.$store.dispatch('incrementAction')
    // },

    // mapActionsで引数なしならこの3行と同じ意味
    // incrementAction(){
    //   this.$store.dispatch('incrementAction')
    // },

    // mapActionsでこのコードが生成される
    // これだと引数を渡せない
    // addCountAction(){
    //   this.$store.dispatch('addCountAction')
    // },
    
    // addCount(){
    //   this.$store.dispatch('addCountAction', {
    //     value: 10
    //   }),

    // mapActionsで引数を取る場合は
    // 別メソッドを用意し、this.action名(引数)でOK
    addCount(){
      this.addCountAction( {
        value: 10
      })
    }
  }
}
</script>

