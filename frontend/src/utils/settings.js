/**
 * 设置管理工具
 */

const DEFAULT_SETTINGS = {
  // 外观设置
  theme: 'light',
  fontSize: 'medium',
  compactMode: false,
  
  // 功能设置
  autoSave: true,
  showThinking: true,
  enableSocratic: false,
  retrievalK: 5,
  temperature: 0.7,
  maxTokens: 2000,
  
  // 高级设置
  enableCache: true,
  debugMode: false,
};

export const getSettings = () => {
  const saved = localStorage.getItem('rag_settings');
  if (saved) {
    try {
      return { ...DEFAULT_SETTINGS, ...JSON.parse(saved) };
    } catch (error) {
      console.error('加载设置失败:', error);
    }
  }
  return DEFAULT_SETTINGS;
};

export const saveSettings = (settings) => {
  localStorage.setItem('rag_settings', JSON.stringify(settings));
  applySettings(settings);
};

export const applySettings = (settings) => {
  // 应用主题
  if (settings.theme === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
  
  // 应用字体大小
  const fontSizeMap = {
    small: '14px',
    medium: '16px',
    large: '18px'
  };
  document.documentElement.style.fontSize = fontSizeMap[settings.fontSize] || '16px';
  
  // 应用紧凑模式
  if (settings.compactMode) {
    document.documentElement.classList.add('compact');
  } else {
    document.documentElement.classList.remove('compact');
  }
};

export const resetSettings = () => {
  localStorage.setItem('rag_settings', JSON.stringify(DEFAULT_SETTINGS));
  applySettings(DEFAULT_SETTINGS);
  return DEFAULT_SETTINGS;
};

// 在应用启动时应用设置
export const initSettings = () => {
  const settings = getSettings();
  applySettings(settings);
  return settings;
};


