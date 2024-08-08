<script lang="ts" setup>

import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

import {useRouter} from 'vue-router'
import { reactive, Reactive } from 'vue';

const router = useRouter()
console.log(router,'router')
const mapdata = reactive(router.options.routes[0].children)

const handleClick = (item) => {
    console.log(item,'item')
    router.push(item.path)
}

</script>

<template>
    <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="manu-container"
        default-active="2"
        text-color="#fff"
    >
        <p class="logo-lg">智能语录</p>
        <template v-for="item in mapdata">
            <el-menu-item @click="handleClick(item)" v-if="item.path == 'asr'" :key="item.meta.id" :index="item.meta.id">
                <el-icon size="20">
                    <component :is="item.meta.icon"></component>
                </el-icon>
                <span>{{ item.meta.name }}</span>
            </el-menu-item>
            <el-menu-item @click="handleClick(item)" v-if="item.path == 'textsum'" :key="item.meta.id" :index="item.meta.id">
                <el-icon size="20">
                    <component :is="item.meta.icon"></component>
                </el-icon>
                <span>{{ item.meta.name }}</span>
            </el-menu-item>
            <el-menu-item @click="handleClick(item)" v-if="item.path == 'exfile'" :key="item.meta.id" :index="item.meta.id">
                <el-icon size="20">
                    <component :is="item.meta.icon"></component>
                </el-icon>
                <span>{{ item.meta.name }}</span>
            </el-menu-item>
            <el-menu-item @click="handleClick(item)" v-if="item.path == 'user'" :key="item.meta.id" :index="item.meta.id">
                <el-icon size="20">
                    <component :is="item.meta.icon"></component>
                </el-icon>
                <span>{{ item.meta.name }}</span>
            </el-menu-item>
        </template>
    </el-menu>
</template>

<style scoped>

.manu-container{
    height: 100%;
    width: 256px;
}

.logo-lg{
    display: grid;
    place-items: center;;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    margin: 0;
    height: 60px;
    color: #545c64;
    background-color: #ffd04b;
}
</style>