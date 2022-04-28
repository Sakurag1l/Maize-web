<!--
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
-->
<template>
  <div class="tool">
    <div class="tool-up">
      <div class="top-text">
        <h1 style="font-size: 35px">
          aaMaize DNA methylation level prediction and analysis
        </h1>
        <h3>
          Introductions ntroductions ntroductions ntroductions
          ntroductionsntroductions ntroductions ntroductions ntroductions
          ntroductionsntroductions ntroductions ntroductions ntroductions
          ntroductions
        </h3>
      </div>
      <div style="margin-top: 50px; height: 330px; text-align: center">
        <a-row>
          <a-col :span="12">
            <div>
              <h2>Choose your methylation type 👇</h2>
              <div>
                <a-select style="width: 120px" v-model="methltype">
                  <a-select-option
                    v-for="value in typelist"
                    :key="value"
                    :value="value"
                  >
                    {{ value }}
                  </a-select-option>
                </a-select>
                <a-button
                  style="margin-top: 6px"
                  type="primary"
                  @click="confirmtype"
                >
                  Confirm
                </a-button>
              </div>
              <a-spin
                style="margin-top: 50px"
                size="large"
                :spinning="loading"
              />
              <a-result
                v-show="!loading"
                status="success"
                title="Successfully Load Model!!"
              />
            </div>
          </a-col>
          <a-col :span="12">
            <div>
              <h2>Paste one sequence(3001bp) here 👇</h2>
              <a-textarea
                v-model="InputSeqs"
                placeholder="Input your Seqs"
                :auto-size="{ minRows: 10, maxRows: 10 }"
              />
              <a-row style="text-align: center">
                <a-col :span="10">
                  <h2 style="margin-top: 6px; font-weight: bold">
                    Or load it from disk:
                  </h2>
                </a-col>
                <a-col :span="6">
                  <a-upload
                    :v-model:file-list="fileList"
                    :max-count="1"
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :beforeUpload="handleChange"
                    @change="changestatue"
                  >
                    <a-button>
                      <a-icon type="upload" />Click to Upload
                    </a-button>
                  </a-upload>
                </a-col>
              </a-row>
              <a-button
                style="margin-top: 6px"
                type="primary"
                block
                :disabled="loading"
                @click="submitseqs"
              >
                Submit
              </a-button>
            </div>
          </a-col>
        </a-row>
      </div>
    </div>
    <div style="width: 80%; margin-left: 12%">
      <h1>{{ `Prediction:  ${preresult}` }}</h1>
      <h1>Heatmap:</h1>
    </div>
    <div id="imgId" @click="openimg" class="showimg">
      <img style="width: 100%; height: 280px" src="../../img/CHG_TN.png" />
      <img style="width: 100%; height: 110px" src="../../img/seqs.png" />
    </div>
  </div>
</template>

<script>
import { ModelPre, getResult } from "../../request/api.js";
// import { UploadOutlined } from "@ant-design/icons-vue";

export default {
  name: "Methylation",
  components: {},

  data() {
    return {
      list1: [],
      typelist: ["CHH", "CHG", "CG"],
      InputSeqs: "",
      loading: true,
      methltype: "CHG",
      isShowImg: false,
      preresult: "",
      fileList: [],
    };
  },
  methods: {
    confirmtype() {
      this.loading = false;
    },
    handleChange(file) {
      console.log(file);
      return false;
    },
    changestatue() {
      console.log(this.fileList);
    },
    submitseqs() {
      let modeldata = {
        seq: "ACCCCC",
        modelName: "test",
      };

      ModelPre(modeldata).then((res) => {
        console.log(res.data);
        setTimeout(() => {
          let taskID = "1907_1649343922600";
          getResult(taskID).then((res) => {
            this.preresult = res.data.result;
            console.log(res);
          });
        }, 2 * 1000);
      });
    },
    openimg() {
      this.isShowImg = !this.isShowImg;
      if (this.isShowImg) {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "160%";
        temp.childNodes[0].style.height = "340px";
        temp.childNodes[1].style.width = "160%";
        temp.childNodes[1].style.height = "160px";
        temp.setAttribute("class", "isopenimg");
      } else {
        let temp = document.getElementById("imgId");
        console.log(temp.childNodes);
        temp.childNodes[0].style.width = "100%";
        temp.childNodes[0].style.height = "280px";
        temp.childNodes[1].style.width = "100%";
        temp.childNodes[1].style.height = "110px";
        temp.setAttribute("class", "showimg");
      }
    },
  },
  created() {},
};
</script>
<style scoped>
.tool {
  height: 1500px;
}
.tool-up {
  width: 80%;
  margin: 0 auto;
}
.top-text {
  text-align: center;
}
.showimg {
  cursor: zoom-in;
  /* width: 80%; */
}
.isopenimg {
  width: 90%;
  margin: 0 auto;
  overflow-x: scroll;
  cursor: zoom-out;
}
.upload-list-inline :deep(.ant-upload-list-item) {
  float: left;
  width: 200px;
  margin-right: 8px;
}
.upload-list-inline [class*="-upload-list-rtl"] :deep(.ant-upload-list-item) {
  float: right;
}
</style>