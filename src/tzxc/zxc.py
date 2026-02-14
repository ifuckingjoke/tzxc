import os
import sys
import time
import signal
from typing import Optional
from getpass import getuser


class Tourter:
    def __init__(self):
        self.username = getuser()
        
    def _block_print(self, signum, frame):
        """Блокирует Ctrl+C"""
        print("\nКуда собрался? Мы ещё не закончили 👿")
    
    def _get_texts(self, lang: str):
        """Возвращает тексты на нужном языке"""
        if lang == "eng":
            return {
                "jason": "Jason",
                "i_counted": "I've... counted it",
                "wrong": "The answer is wrong, think correctly.",
                "who_taught": "Who taught you to count? AHAHAHAHA. I said count correctly.",
                "said_correctly": "I SAID COUNT CORRECTLY",
                "final_warning": "I AM GIVING YOU A FINAL WARNING",
                "crazy": "What? Did you go crazy so quickly? It's okay, try again",
                "well_done": "Well done...",
                "start_over": "Shall we start over?"
            }
        else:  # русский по умолчанию
            return {
                "jason": "Джейсон",
                "i_counted": "Я... досчитал",
                "wrong": "Ответ неверный, считай правильно.",
                "who_taught": "Кто тебя учил считать? АХАХАХА. Я сказал считать правильно.",
                "said_correctly": "Я СКАЗАЛ СЧИТАЙ ПРАВИЛЬНО",
                "final_warning": "Я ДАЮ ПОСЛЕДНЕЕ ПРЕДУПРЕЖДЕНИЕ",
                "crazy": "Чего? Ты так быстро сошёл с ума? Нечего страшного, попробуй снова",
                "well_done": "Молодец...",
                "start_over": "Начнём сначала?"
            }
    
    def _shutdown(self):  
        if sys.platform == "win32":
            os.system("shutdown /r /t 0")
        elif sys.platform == "linux":
            os.system("sudo reboot")
    
    def zxc(self, delay: int, 
            infinity: bool = False, 
            hard_mode: bool = False, 
            ctrl_off: bool = False, 
            crazy_mode: bool = False, 
            lang: str = 'ru'):
        """
        Основной метод игры
        
        Args:
            delay: Задержка между действиями
            infinity: Бесконечный режим (после 6 начинается заново)
            hard_mode: Требуется вводить ответы
            ctrl_off: Блокировать Ctrl+C
            crazy_mode: Более агрессивные сообщения
            lang: Язык ('ru' или 'eng')
        """
        
        texts = self._get_texts(lang)
        jason = texts["jason"]
        
        # Настройка перехвата Ctrl+C
        original_sigint = None
        if ctrl_off:
            original_sigint = signal.getsignal(signal.SIGINT)
            signal.signal(signal.SIGINT, self._block_print)
        
        try:
            x = 1000
            uncorrect_answers = 0
            
            while True:
                if hard_mode:
                    # Hard mode: ждём ввод пользователя
                    print(f"{jason}: {x} - 7?")
                    
                    try:
                        answer = int(input("Ответ: "))
                    except (ValueError, TypeError):
                        print(f"{jason}: {texts['crazy']}")
                        continue
                    
                    if answer != x - 7:
                        # Неправильный ответ
                        uncorrect_answers += 1
                        
                        if uncorrect_answers == 1:
                            print(f"{jason}: {texts['wrong']}")
                        elif uncorrect_answers == 2:
                            print(f"{jason}: {texts['who_taught']}")
                        elif uncorrect_answers == 3:
                            print(f"{jason}: {texts['said_correctly']}")
                        elif uncorrect_answers == 4:
                            print(f"{jason}: {texts['final_warning']}")
                        elif uncorrect_answers >= 5:
                            self._shutdown()
                            break
                        
                        time.sleep(delay)
                        continue
                    else:
                        # Правильный ответ
                        x -= 7
                        uncorrect_answers = 0  # сбрасываем счётчик ошибок
                        
                else:
                    # Обычный режим: автоматический счёт
                    time.sleep(delay)
                    print(f"{jason}: {x} - 7?")
                    x -= 7
                    
                    time.sleep(delay)
                    print(f"{self.username}: {x}")
                
                # Проверка окончания
                if x == 6:
                    print(f"{self.username}: {texts['i_counted']}")
                    
                    if infinity:
                        time.sleep(delay + 2)
                        print(f"{jason}: {texts['well_done']} {texts['start_over']}")
                        x = 1000
                        uncorrect_answers = 0
                        time.sleep(delay + 1)
                    else:
                        break
                        
        finally:
            # Восстанавливаем обработчик Ctrl+C
            if ctrl_off and original_sigint is not None:
                signal.signal(signal.SIGINT, original_sigint)