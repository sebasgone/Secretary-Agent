from app.services.rag.rag_engine import rag_bot


def rag_manager(user_input):
    bot=rag_bot()
    return bot.invoke(user_input).content

