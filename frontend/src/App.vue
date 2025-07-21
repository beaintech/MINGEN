<template>
  <div class="app">
    <h1>Astrology & Feng Shui Report Generator</h1>
    <form @submit.prevent="generateBasic">
      <label>Name: <input v-model="formData.name" /></label>
      <label>Birthday: <input type="date" v-model="formData.birthday" /></label>
      <label>Birth Time: <input type="time" v-model="formData.time" /></label>
      <label>Birthplace: <input v-model="formData.birthplace" /></label>
      <label>Gender: 
        <select v-model="formData.gender">
          <option value="Not Provided" selected>Not Provided</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
      </label>
      <br>
      <br>
    </form>

    <button v-if="!basicReport" @click="generateBasic" type="submit">Generate Basic Report (Free)</button>
    <div v-else v-html="basicReport" class="report"></div>

    <button v-if="!extraReport" @click="generateExtra" type="submit">Unlock Love & Wealth Report (Paid)</button>
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
// const cleanMarkdown = (text) => {
//   return text.replace(/```markdown|```/g, '')
// }

const cleanMarkdown = (rawText) => {
  if (!rawText) return ''

  return rawText
    // 去掉代码块标记
    .replace(/```(html|markdown)?/g, '')
    // 去掉 Markdown 的标题符号
    .replace(/^#+\s?/gm, '')
    // 去掉多余的分隔线
    .replace(/^---$/gm, '')
    // 修剪空白
    .trim()
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
