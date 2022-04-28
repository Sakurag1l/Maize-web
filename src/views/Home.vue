<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="home">
    <div id="components-layout-demo-basic">
      <a-layout>
        <a-layout-content>
          <div
            class="top-text"
            style="width: 70%; margin-top: 10px; margin-bottom: 10px"
          >
            <a-card>
              <p>Card content Card contentCard contentCard</p>
            </a-card>
          </div>
          <div>
            <p>Something About Paper</p>
          </div>
        </a-layout-content>
      </a-layout>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Home",
  components: {},
  data() {
    return {
      list1: [],
    };
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
#components-layout-demo-basic {
  text-align: center;
}
#components-layout-demo-basic .ant-layout-content {
  background: white;
  color: black;
}

.home {
  text-align: center;
  height: 1000px;
  width: 80%;
  margin: 0 auto;
}
.top-text {
  display: flex;
}
</style>