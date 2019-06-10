import tkinter as tk
import GameFunctions as Gf

class board:
    def __init__(self, window):
        self.window = window
        self.window.geometry('265x300')
        self.window.config(bg='White')
        self.Gf = Gf.gameFunctions(self.window)
        self.window.title("Tic-Tac-Toe")
        self.__buttons__(window)
        self.window.mainloop()

    def __buttons__(self, window):
        '''
        These are all the visual components used for the GUI display
        All labels, buttons, and entries are stored here and altered
        in the Game Functions library located in this directory.
        '''

        # Defining window and spacing options for GUI window
        self.window = window
        m_toppad  = 5
        m_leftpad = 12
        m_font = ('ariel',14)
        m_butHgt = 3
        m_butWid = 6

        # Label information
        self.lbl_gameIntro = tk.Label(self.window,
                                      text="Everett's Amazing Tic-Tac-Toe Game",
                                      font=m_font, 
                                      bg='White',
                                      width=28)

        # Button information from top left accross then down to bottom right
        # TOP
        self.btn_topLft = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_topLft))
        
        self.btn_topMid = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_topMid))

        self.btn_topRgt = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_topRgt))

        # MIDDLE
        self.btn_cenLft = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_cenLft))

        self.btn_cenMid = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_cenMid))

        self.btn_cenRgt = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_cenRgt))

        # BOTTOM
        self.btn_botLft = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                   width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_botLft))

        self.btn_botMid = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_botMid))

        self.btn_botRgt = tk.Button(self.window,
                                    text='-',
                                    font=m_font,
                                    bg='White',
                                    width=m_butWid,
                                    height=m_butHgt,
                                    command=lambda:self.Gf.playerSelect(self.btn_botRgt))
        
        # Main Label Positional Information
        self.lbl_gameIntro.grid(row=0, 
                                column=0,
                                columnspan=35,
                                padx=(m_leftpad*(5/12),0),
                                pady=(m_toppad,0))

        # Button Positional Information
        self.btn_topLft.grid(row=1,
                             column=0,
                             padx=(m_leftpad,0))

        self.btn_topMid.grid(row=1,
                             column=1)

        self.btn_topRgt.grid(row=1,
                             column=2)

        self.btn_cenLft.grid(row=2,
                             column=0,
                             padx=(m_leftpad,0))
        
        self.btn_cenMid.grid(row=2,
                             column=1)

        self.btn_cenRgt.grid(row=2,
                             column=2)

        self.btn_botLft.grid(row=3,
                             column=0,
                             padx=(m_leftpad,0))

        self.btn_botMid.grid(row=3,
                             column=1)

        self.btn_botRgt.grid(row=3,
                             column=2)