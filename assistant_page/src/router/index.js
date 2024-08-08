import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/Main.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
      children: [
        {
          path:'asr',
          meta: {
            id: '1', name: '语音识别', icon: 'Microphone', path: '/asr', describe: '语音识别，选择需要进行识别的语言，可上传音频文件或直接录音，识别结果将显示在页面上。'
          },
          component: () => import('../views/asr/ASR.vue')
        },
        {
          path: 'textsum',
          meta: {
            id: '2', name: '文本处理', icon: 'document', path: '/textsum', describe: '文本处理，上传文本或直接输入文本，可将口语化的文本转换为书面文本。'
          },
          component: () => import('../views/textsum/Textsum.vue')
        },
        {
          path: 'exfile',
          meta: {
            id: '3', name: '音频转换', icon: 'Refresh', path: '/exfile', describe: '音频转换，上传或录音音频文件，可选择指定的格式保存。'
          },
          component: () => import('../views/exfile/Exfile.vue')
        },
        {
          path: 'user',
          meta: {
            id: '4', name: '账号管理', icon: 'User', path: '/user', describe: '用户管理，可重置用户密码，管理用户信息'
          },
          component: () => import('../views/user/User.vue')
        }
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/TestView.vue')
    }
  ]
})

export default router
