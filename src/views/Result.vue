<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="result">
    <div style="margin: 15px; margin: 0 auto; width: 80%; text-align: center">
      <h1>This is an result page</h1>
    </div>
    <div style="width: 80%; margin: 0 auto; text-align: center">
      <a-row>
        <a-col :span="12">
          <div>
            <p style="margin-top: 15px; font-size: 25px">
              We trained three types of methylation CG/CHG/CHH models and
              obtained ROC curves.
            </p>
          </div>
        </a-col>
        <a-col :span="12">
          <img style="width: 100%" src="../img/roc.png" />
        </a-col>
      </a-row>
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 15px">
      <p style="font-size: 25px">
        We predict the model in the population and visualize the meaningful
        sequences after analysis. In addition, some motifs leading to high
        methylation in maize were found in the predicted TP.
      </p>
    </div>
    <div>
      <img style="width: 100%; height: 280px" src="../img/CHG_TN.png" />
      <img style="width: 100%; height: 150px" src="../img/seqs.png" />
    </div>
    <div style="width: 80%; margin: 0 auto; margin-top: 15px">
      <p style="font-size: 25px">
        In addition, some motifs leading to high methylation in maize were found
        in the predicted TP.
      </p>
    </div>
    <img style="width: 100%; height: 100px" src="../img/atat.png" />
    <div style="width: 80%; margin: 0 auto; margin-top: 15px">
      <p style="font-size: 25px">
        In addition, some motifs leading to high methylation in maize were found
        in the predicted TP.
      </p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Result",
  components: {},
  data() {
    return {};
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
.result {
  height: 1500px;
  /* text-align: center; */
  /* width: 80%; */
  margin: 0 auto;
}
</style>