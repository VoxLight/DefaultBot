import discord
from discord.ext import commands

# Locals
from os import getcwd
import os
import numpy as np
import scipy.misc as smp

# pip
from PIL import Image, ImageDraw



class Drawing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.files = getcwd()+"\\cogs\\command_files\\drawing\\"
        self.ext = ".png"
        self.res = (100, 100)
        self.color = (255, 255, 255, 255)
        self.npres = self.res + (3,)
        print("Drawing cog loaded.")

    def get_fp(self, name):
        return self.files+name+self.ext

    def get_image(self, fp):
        return Image.open(fp)

    def save_image(self, fp, image=None):
        # This function saves a pixel bitmap to file.
        # Not passing a bitmap saves a black i
        img = image if image != None else Image.new("RGB", self.res, color=self.color)
        img.save(fp)

    @commands.command(name="view")
    async def get_picture(self, ctx, name: str):
        fp = self.get_fp(name)
        
        await ctx.send("", file=discord.File(fp))

    @commands.command(name="draw")
    async def draw_picture(self,ctx,name:str,x:int,y:int,r:int=255,g:int=255,b:int=255):
        xy = (x, y)
        rgb = (r, g, b)
        fp = self.get_fp(name)
        img = self.get_image(fp)
        img.putpixel(xy, rgb)
        img.save(fp)
        await ctx.send("", file=discord.File(fp))

    @commands.command(name="fill")
    async def fill_picture(self,ctx,name:str,x:int,y:int,x2:int,y2:int,r:int=255,g:int=255,b:int=255):
        xy = (x, y)
        xy2 = (x2, y2)
        rgb = (r, g, b)
        fp = self.get_fp(name)
        img = self.get_image(fp)
        draw = ImageDraw.Draw(img)
        draw.rectangle(xy + xy2, fill=rgb)
        img.save(fp)
        await ctx.send("", file=discord.File(fp))

    @commands.command(name="line")
    async def line_picture(self,ctx,name:str,x:int,y:int,x2:int,y2:int,r:int=255,g:int=255,b:int=255, w: int = 1):
        xy = (x, y)
        xy2 = (x2, y2)
        rgb = (r, g, b)
        fp = self.get_fp(name)
        img = self.get_image(fp)
        draw = ImageDraw.Draw(img)
        draw.line(xy + xy2, width=w, fill=rgb)
        img.save(fp)
        await ctx.send("", file=discord.File(fp))

    @commands.command(name="poly")
    async def poly_picture(self, ctx, name: str):
        pass
    
    @commands.command(name="new")
    async def new_picture(self,ctx,name:str, h:int=None, w:int=None):
        if h == None or w == None:
            h, w = self.res
        fp = self.get_fp(name)
        img=Image.new("RGBA", (h, w))
        self.save_image(fp,image=img)
        await ctx.send("Saved your new image: "+name)

    @commands.command(name="size")
    async def size_picture(self,ctx,name:str):
        fp = self.get_fp(name)
        img = self.get_image(fp)
        await ctx.send(img.size)

    @commands.command(name="pictures")
    async def get_pictures(self, ctx):
        pics = os.listdir(self.files)
        await ctx.send(str(pics))

    

        

    @commands.command()
    async def coords(self, ctx):
        await ctx.send("""
The Python Imaging Library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner. Note that the coordinates refer to the implied pixel corners; the centre of a pixel addressed as (0, 0) actually lies at (0.5, 0.5).
Coordinates are usually passed to the library as 2-tuples (x, y). Rectangles are represented as 4-tuples, with the upper left corner given first. For example, a rectangle covering all of an 800x600 pixel image is written as (0, 0, 800, 600).
        """)

    



def setup(bot):
    bot.add_cog(Drawing(bot))