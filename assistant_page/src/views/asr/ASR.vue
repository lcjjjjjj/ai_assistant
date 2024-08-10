<script setup>
import Panel from '@/components/Panel.vue';
import { ref } from 'vue';
import { ElMessageBox } from 'element-plus';

const result = ref('');

const handleExceed = (files, uploadFiles) => {
    console.log('限制上传', files, uploadFiles)
    ElMessageBox.alert('只能上传一个文件，如有需要请删除上一个文件再进行上传','温馨提示',{confirmButtonText: '确定',})
}
</script>

<template>
    <Panel />
    <div class="app-area">
        <el-upload
            class="upload-demo"
            drag
            action=" http://localhost:5000/upload"
            multiple
            accept=".wav, .mp3"
            :limit="1"
            :on-exceed="handleExceed"
        >
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
                拖拽文件到此处 或 <em>点击上传</em>
            </div>
        </el-upload>
    </div>
    <div class="button-area">
        <div class="left-area">
            
        </div>
        <div class="right-area">
            <el-button type="primary" round @Click="onClick">开始</el-button>
            <el-button type="warning" round>停止</el-button>
            <el-button type="danger" round>重试</el-button>
            <el-button type="success" round>保存</el-button>
        </div>
    </div>
    <div class="result-area">
        <el-input
        v-model="result"
        style="width: 100%;"
        :rows="13"
        type="textarea"
        placeholder="识别结果"
        />
    </div>
</template>

<style scoped>
.app-area {
    padding-top: 15px;
    padding-left: 25%;
    padding-right: 25%;
    padding-bottom: 15px;
}

.button-area {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
    padding-left: 25%;
    padding-right: 25%;
    padding-bottom: 15px;
    
}

.result-area {
    
    padding-top: 15px;
    padding-left: 25%;
    padding-right: 25%;
    padding-bottom: 15px;
    
}
</style>