<template>
  <div class="app">
    <h1>星命风水报告生成器</h1>
    <form @submit.prevent="generateBasic">
      <label>姓名: <input v-model="formData.name" /></label>
      <label>生日: <input type="date" v-model="formData.birthday" /></label>
      <label>出生时间: <input type="time" v-model="formData.time" /></label>
      <label>出生地: <input v-model="formData.birthplace" /></label>
      <label>性别: 
        <select v-model="formData.gender">
          <option value="未提供" selected>未提供</option>
          <option value="男">男</option>
          <option value="女">女</option>
        </select>
      </label>
      <br>
      <br>

    </form>
    <button v-if="!basicReport" @click="generateBasic" type="submit">生成基础报告 (免费)</button>
    <div v-else v-html="basicReport" class="report"></div>

    <button v-if="!extraReport" @click="generateExtra" type="submit">解锁情感与财富报告 (付费)</button>
    <div v-else v-html="extraReport" class="report"></div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { marked } from 'marked'

const formData = ref({
      name: "",
      gender: "未提供",
      birthday: "",
      time: "",
      birthplace: ""
    })

const basicReport = ref('')
const extraReport = ref('')

// GPT 返回的 result
const cleanMarkdown = (text) => {
  return text.replace(/```markdown|```/g, '')
}

const API_BASE = "https://starseed-api.onrender.com"

const generateBasic = async () => {
  try {
    // const res = await axios.post('http://127.0.0.1:8000/generate-basic-report', formData.value)
    const res = await axios.post(`${API_BASE}/generate-basic-report`, formData.value)
    console.log('后端返回的数据:', res.data.result) 
    basicReport.value = cleanMarkdown(res.data.result)  // 处理返回的HTML
    
  } catch (err) {
    console.error('Extra Report Error:', err)
    extraReport.value = '<p>高级报告加载失败</p>'
   }   
}

const generateExtra = async () => {
  try {
      // const res = await axios.post('http://127.0.0.1:8000/generate-extra-report', formData.value)
      const res = await axios.post(`${API_BASE}/generate-extra-report`, formData.value)
      console.log('后端返回的数据:', res.data.result) 
      extraReport.value = cleanMarkdown(res.data.result)
    } catch (err) {
     console.error('Error submitting:', err)
     response.value = { error: '提交失败，请检查服务端是否运行' }
   }   
  }
  
</script>

<style scoped>
.report table {
  width: 100%;
  border-collapse: collapse;
}

.report th, .report td {
  border: 1px solid #ccc;
  padding: 8px;
}

.container {
  max-width: 75%;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
  font-family: Arial, sans-serif;
}
input, button {
  display: block;
  width: 100%;
  margin-bottom: 15px;
  padding: 8px;
  font-size: 16px;
}
button {
  background-color: #409eff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
button:hover {
  background-color: #66b1ff;
}

.markdown-table table {
  width: 100%;
  table-layout: fixed;
}

.markdown-table td:first-child {
  width: 25%;
  font-weight: bold;
}

</style>
